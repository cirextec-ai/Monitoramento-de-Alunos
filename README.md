# 🎓 Monitoramento de Alunos em Tempo Real

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.14-orange?logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-blue?logo=opencv&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?logo=googlecolab&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📝 Descrição do Projeto

Protótipo de **monitoramento e reconhecimento em tempo real de alunos** através de imagens do rosto, utilizando **aprendizado de máquina** e **visão computacional**.

O sistema captura imagens da câmera do notebook, extrai **embeddings faciais** e compara com um banco de dados previamente treinado para identificar os alunos em tempo real.

**Problema resolvido:**  
Monitoramento manual da presença e atenção dos alunos é demorado e sujeito a erros. Este protótipo permite **identificação rápida e confiável** de cada aluno em tempo real.

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Ícone | Função |
|------------|-------|--------|
| Python 3.12 | ![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white) | Linguagem principal do projeto |
| TensorFlow/Keras | ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.14-orange?logo=tensorflow&logoColor=white) | Treinamento e inferência de modelos de reconhecimento facial |
| OpenCV | ![OpenCV](https://img.shields.io/badge/OpenCV-4.8-blue?logo=opencv&logoColor=white) | Captura de vídeo e processamento de imagens |
| Google Colab | ![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?logo=googlecolab&logoColor=white) | Ambiente de desenvolvimento e teste do protótipo |

---

## 🏛 Arquitetura do Sistema

```text
┌───────────────────┐
│ Webcam do Notebook│
└────────┬──────────┘
         │ Captura imagens
         ▼
┌───────────────────┐
│ Pré-processamento │
│ - Redimensionamento│
│ - Normalização    │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Modelo CNN /      │
│ Embeddings Faciais│
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Banco de Embeddings│
│ de Alunos         │
└────────┬──────────┘
         │ Comparação / Reconhecimento
         ▼
┌───────────────────┐
│ Resultado em Tempo│
│ Real: Aluno ID    │
└───────────────────┘

⚡ Funcionalidades

🎥 Captura de vídeo em tempo real da webcam do notebook.

🖼 Pré-processamento automático das imagens (redimensionamento, normalização).

🧠 Reconhecimento facial utilizando embeddings faciais e comparação com banco de dados.

📊 Treinamento de modelo customizado com dataset de rostos dos alunos.

📄 Logs de identificação em tempo real e possibilidade de salvar histórico.

🚀 Como Executar

Clone o repositório:

git clone https://github.com/seu-usuario/monitoramento-alunos.git
cd monitoramento-alunos
Abra os notebooks no Google Colab:

dataset_preparation.ipynb – Cria o dataset de rostos.

train_model.ipynb – Treina o modelo de reconhecimento facial.

real_time_monitoring.ipynb – Executa o monitoramento em tempo real.

Estrutura de pastas recomendada:
processed_rosto_alunos/
└─ estagio/rostos_csv/rostos_alunos/

📁 Estrutura do Repositório

monitoramento-alunos/
│
├─ processed_rosto_alunos/     # Dataset de imagens de rostos
├─ notebooks/                  # Notebooks de preparação, treino e monitoramento
├─ models/                     # Modelos treinados (.h5)
├─ README.md                   # Este arquivo
└─ requirements.txt            # Dependências do projeto

📌 Observações

O protótipo funciona com a câmera do notebook (no Colab, é necessário permitir acesso via navegador).

Treinar com imagens bem organizadas e iluminadas aumenta a precisão do reconhecimento.

Funciona melhor com uma única pessoa por frame, mas pode ser adaptado para múltiplos rostos.

🛡 Licença

MIT License – sinta-se livre para usar, modificar e contribuir com este protótipo.

👤 Autor

Sergio Ademir Rocha do Carmo

---
