from django.shortcuts import render
from acoes.models import Acao
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import base64
import io


# Função para limpar o banco de dados
def limpar_banco_de_dados():
    # Use o método de exclusão em massa para excluir todos os objetos do modelo Acao
    Acao.objects.all().delete()

#limpar_banco_de_dados()

def formulario(request):
    return render(request,'formulario_acoes.html')

# Buscador de dados WEB
def buscador_acoes(request):
    Acao.objects.all().delete()
    # Se a requisição for do tipo GET, renderizar o template html sem dados
    if request.method == "GET":
        return render(request,"formulario_acoes.html")

    if request.method == 'POST':
        acoes = request.POST.get('acoes').split(', ')  # Recebe as ações do formulário

        #acoes = ['PETR4.SA', 'GOLL4.SA', 'BOVA11.SA']
        dados_acoes = {}
        dados = []
        for acao in acoes:
            ticker = yf.Ticker(acao)
            historico = ticker.history(period='3y')

            # Calcula média, desvio padrão e coeficiente de variação            
            media = round(historico['Close'].mean(), 2)
            desvio_padrao = round(historico['Close'].std(), 2)
            coef_variacao = round((desvio_padrao / media) * 100, 2)
                        
            dados_acoes[acao] = {'codigo': acao, 'media': media, 'desvio_padrao': desvio_padrao, 'coef_variacao': coef_variacao}
            dados.append(dados_acoes[acao])

        # Populando Banco de Dados
        for dado in dados:
            nome = dado['codigo']
            media = dado['media']
            desvio_padrao = dado['desvio_padrao']
            coef_variacao = dado['coef_variacao']

            novo_dados = Acao(nome=nome, media=media, desvio_padrao=desvio_padrao, coef_variacao=coef_variacao)
            novo_dados.save()
                
        # Buscando dados do banco de dados
        acoes = Acao.objects.all()
        
        # Criando gráfico   
        media = []
        desvp = []
        coef_var = []
        categorias = []
        for categ in acoes:
            dados_media = categ.media
            dados_desvp = categ.desvio_padrao
            dados_coef_var = categ.coef_variacao
            dados_nome = categ.nome
                    
            # Adcionando dados as listas
            media.append(dados_media)
            desvp.append(dados_desvp)
            coef_var.append(dados_coef_var)
            categorias.append(dados_nome)
        
        legendas = ['Média', 'Desvio', 'CV']
        listas_dados = [media, desvp, coef_var]

        num_categorias = len(categorias)
        largura = 0.2  # largura das barras

        fig, ax = plt.subplots()
        #fig.set_size_inches(10, 5)  # Define o tamanho da figura

        posicoes = np.arange(num_categorias)  # Posições das categorias no eixo x

        for i in range(len(listas_dados)):
            barras = ax.bar(posicoes + i * largura, listas_dados[i], largura, label=f'{legendas[i]}')

        ax.set_xticks(posicoes + largura * (len(listas_dados) - 1) / 2)  # Posicionamento dos ticks no eixo x
        ax.set_xticklabels(categorias)
        ax.legend()

        # Construindo a imagem
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png).decode('utf-8')
            
        return render(request, 'resultado_acoes.html', {'acoes': acoes, 'graphic': graphic})


def grafico_barras(request):
    
    '''
    
    categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
    dados = [[10, 10, 10], [20, 20, 20], [30,30,30]]
    legendas = ['A', 'B', 'C']
    
    '''
    
    # Buscando dados do banco de dados
    acoes = Acao.objects.all()
    
    # Dados de exemplo        
    media = []
    desvp = []
    coef_var = []
    categorias = []
    for categ in acoes:
        dados_media = categ.media
        dados_desvp = categ.desvio_padrao
        dados_coef_var = categ.coef_variacao
        dados_nome = categ.nome
                
        # Adcionando dados as listas
        media.append(dados_media)
        desvp.append(dados_desvp)
        coef_var.append(dados_coef_var)
        categorias.append(dados_nome)
    
    legendas = ['A', 'B', 'C']
    listas_dados = [media, desvp, coef_var]

    num_categorias = len(categorias)
    largura = 0.2  # largura das barras

    fig, ax = plt.subplots()

    posicoes = np.arange(num_categorias)  # Posições das categorias no eixo x

    for i in range(len(listas_dados)):
        barras = ax.bar(posicoes + i * largura, listas_dados[i], largura, label=f'Dados {legendas[i]}')

    ax.set_xticks(posicoes + largura * (len(listas_dados) - 1) / 2)  # Posicionamento dos ticks no eixo x
    ax.set_xticklabels(categorias)
    ax.legend()

    # Construindo a imagem
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'graficos.html', {'graphic': graphic})


#limpar_banco_de_dados()


 

