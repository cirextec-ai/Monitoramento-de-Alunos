from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Monitoramento de Alunos!")
