import uvicorn
import cv2
import numpy as np
import base64
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

# Importações do seu projeto PyTorch (separe o código de inferência)
import torch
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights

# Defina a quantidade de classes que seu modelo foi treinado
NUM_CLASSES = 2 # Ajuste para o número correto de alunos/classes
# Mapeamento de classe para nome (AJUSTE CONFORME SEU DATASET)
CLASS_NAMES = {
    0: "Aluno A",
    1: "Aluno B",
    # Adicione mais conforme o seu projeto
}

# --- 1. CARREGAMENTO DO MODELO PYTORCH ---
def load_model_for_inference(model_path="caminho/para/seu/modelo_pesos.pth"):
    """
    Carrega o modelo PyTorch e o coloca em modo de avaliação.
    
    Atenção: Substitua esta função pelo seu código de carregamento
    exato (ResNet-18 ou VGG-16) e defina o caminho correto.
    """
    try:
        # Inicializa o modelo (Exemplo com ResNet-18)
        model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
        # Substitui a última camada para o seu número de classes
        num_ftrs = model.fc.in_features
        model.fc = torch.nn.Linear(num_ftrs, NUM_CLASSES)
        
        # Carrega os pesos salvos do seu treinamento
        # model.load_state_dict(torch.load(model_path))
        
        model.eval() # Modo de inferência
        print("Modelo PyTorch carregado com sucesso.")
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo PyTorch: {e}")
        # Retorna um modelo "mock" ou lance o erro fatal
        return None

# Carrega o modelo PyTorch globalmente
model = load_model_for_inference()

# Define as transformações de pré-processamento (devem ser as mesmas do treino)
model_transform = transforms.Compose([
    transforms.Resize((224, 224)), # Use o tamanho exato da sua entrada
    transforms.ToTensor(),
    # Use as mesmas médias e desvios do seu treinamento
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

app = FastAPI()

# Permite que o front-end (provavelmente em outra porta) se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Mude para o endereço específico do seu front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/video")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Conexão WebSocket estabelecida.")
    try:
        # Loop para receber frames do cliente
        while True:
            # Recebe o frame em formato de texto (string Base64)
            data = await websocket.receive_text()
            
            # O front-end envia uma string como: "data:image/jpeg;base64,..."
            header, encoded_data = data.split(',', 1)
            
            # Decodifica a string Base64 para bytes
            frame_bytes = base64.b64decode(encoded_data)
            
            # Converte os bytes em um array NumPy (imagem) usando OpenCV
            np_array = np.frombuffer(frame_bytes, np.uint8)
            frame_cv2 = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

            if frame_cv2 is None:
                print("Aviso: Falha ao decodificar o frame.")
                continue
            
            # --- 2. LÓGICA DE INFERÊNCIA DE RECONHECIMENTO DE PESSOAS ---
            
            # 2.1. Simulação/Implementação da DETECÇÃO (usando OpenCV ou outro detector)
            # Como seu modelo parece ser de CLASSIFICAÇÃO (ResNet/VGG), 
            # você precisará de um detector inicial (YOLO, Haar Cascade, etc.)
            
            # Exemplo (Simulação de uma detecção)
            # Se a sua ResNet faz a classificação de uma ÚNICA pessoa na imagem:
            
            # Converte para PIL Image e aplica as transformações
            pil_image = Image.fromarray(cv2.cvtColor(frame_cv2, cv2.COLOR_BGR2RGB))
            input_tensor = model_transform(pil_image).unsqueeze(0)

            results = []
            
            if model is not None:
                with torch.no_grad():
                    # 2.2. Inferência (Classificação)
                    output = model(input_tensor)
                    
                    # Calcula a probabilidade e a classe predita
                    probabilities = torch.softmax(output, dim=1)[0]
                    confidence, predicted_class_idx = torch.max(probabilities, 0)
                    
                    class_name = CLASS_NAMES.get(predicted_class_idx.item(), "Desconhecido")
                    conf_value = confidence.item()
                    
                    # 2.3. Cria um resultado (simulamos as coordenadas para a tela inteira)
                    if conf_value > 0.8: # Somente se tiver alta confiança
                        results.append({
                            'box': [0, 0, frame_cv2.shape[1], frame_cv2.shape[0]], # [x, y, w, h]
                            'nome': class_name,
                            'conf': f"{conf_value:.2f}"
                        })
            
            # --- 3. RETORNO DOS RESULTADOS ---
            
            # Envia a lista de resultados (em formato JSON) de volta ao front-end
            await websocket.send_text(json.dumps(results))

    except Exception as e:
        print(f"Erro na conexão WebSocket ou processamento: {e}")
    finally:
        print("Conexão WebSocket encerrada.")
        await websocket.close()

if __name__ == "__main__":
    # Comando para rodar: uvicorn main:app --reload
    print("Iniciando o servidor FastAPI...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)