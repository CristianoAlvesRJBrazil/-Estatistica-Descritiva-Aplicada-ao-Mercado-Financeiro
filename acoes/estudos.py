from django.shortcuts import render
from acoes.models import Acao
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


# Função para limpar o banco de dados
def limpar_banco_de_dados():
    # Use o método de exclusão em massa para excluir todos os objetos do modelo Acao
    Acao.objects.all().delete()

limpar_banco_de_dados()

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
            historico = ticker.history(period='5y')

            # Calcula média, desvio padrão e coeficiente de variação
            media = round(historico['Close'].mean(), 2)
            desvio_padrao = round(historico['Close'].std(), 2)
            coef_variacao = round((desvio_padrao / media) * 100, 2)

            dados_acoes[acao] = {'codigo': acao, 'media': media, 'desvio_padrao': desvio_padrao, 'coef_variacao': coef_variacao}
            dados.append(dados_acoes[acao])
                
        for dado in dados:
            nome = dado['codigo']
            media = dado['media']
            desvio_padrao = dado['desvio_padrao']
            coef_variacao = dado['coef_variacao']
            

            novo_dados = Acao(nome=nome, media=media, desvio_padrao=desvio_padrao, coef_variacao=coef_variacao)
            novo_dados.save()
            
            # Dados
            categorias = acoes
            dados = dados_acoes[acao]
        
        # Criando o gráfico de barras para cada categoria no mesmo plano cartesiano
        barWidth = 0.2
        x = np.arange(len(acoes))

        for i, usuario in enumerate(dados_acoes[acao]):
            valores = dados_acoes[acao]
            plt.bar(x + i * barWidth, valores, width=barWidth, align='center', label=usuario)

        # Adicionando rótulos aos eixos
        plt.xlabel('Acoes')
        plt.ylabel('Valores')

        # Adicionando título ao gráfico
        plt.title('Gráfico de Barras com Várias Categorias e Valores')

        # Adicionando legendas
        plt.xticks(x + barWidth * (len(dados_acoes[acao]) - 1) / 2, acoes)
        plt.legend()

        # Exibindo o gráfico
        plt.show()
        
        
        categorias = ['A', 'B', 'C', 'D']
        dados = {'Alice': [4, 6, 5, 3], 'Bob': [7, 8, 6, 9], 'Carol': [2, 5, 3, 7]}

        # Criando o gráfico de barras para cada categoria no mesmo plano cartesiano
        barWidth = 0.2
        x = np.arange(len(categorias))

        for i, usuario in enumerate(dados):
            valores = dados[usuario]
            plt.bar(x + i * barWidth, valores, width=barWidth, align='center', label=usuario)

        # Adicionando rótulos aos eixos
        plt.xlabel('Categorias')
        plt.ylabel('Valores')

        # Adicionando título ao gráfico
        plt.title('Gráfico de Barras com Várias Categorias e Valores')

        # Adicionando legendas
        plt.xticks(x + barWidth * (len(dados) - 1) / 2, categorias)
        plt.legend()

        # Exibindo o gráfico
        plt.show()
        
        
    # Criar um gráfico de linhas com os preços das ações
    plt.figure(figsize=(10, 6))
    plt.bar(petr4_hist, label="PETR4")
    plt.plot(bova11_hist, label="BOVA11")
    plt.title("Preços de Fechamento das Ações da Petrobras e do Ibovespa")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.legend()
    plt.grid()
        
    
    acoes = Acao.objects.all()
    
    return render(request, 'resultado_acoes.html', {'acoes': acoes})


#Função para buscar os dados no banco de dados
def tabela_acoes(request):
    acoes = Acao.objects.all()
    return render(request, 'resultado_acoes.html', {'acoes': acoes})


'''
def capturar_acoes():
    
    pass


def tabela_acoes():
    
    pass

'''
python
import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [7, 3, 12, 5]

# Criando o gráfico de barras
plt.bar(categorias, valores)

# Adicionando rótulos aos eixos
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Adicionando título ao gráfico
plt.title('Exemplo de Gráfico de Barras')

# Exibindo o gráfico
plt.show()


# Criar um gráfico de linhas com os preços das ações
plt.figure(figsize=(10, 6))
plt.plot(petr4_hist, label="PETR4")
plt.plot(bova11_hist, label="BOVA11")
plt.title("Preços de Fechamento das Ações da Petrobras e do Ibovespa")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.legend()
plt.grid()

# Converter o gráfico em uma imagem PNG codificada em base64
buffer = BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
graphic = base64.b64encode(image_png)
graphic = graphic.decode("utf-8")

# Renderizar o template html e passar os dados como argumentos
return render_template("index.html", corr=corr, graphic=graphic)




import matplotlib.pyplot as plt
import numpy as np



# Dados de exemplo
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
num_listas = 3
dados = [[20, 35, 30, 35], [25, 32, 34, 20], [30, 23, 32, 25]]

# Configuração do gráfico de barras
largura_total = 0.8
largura_barra = largura_total / num_listas
indice = np.arange(len(categorias))

# Criar as barras para cada lista de dados
for i in range(num_listas):
    plt.bar(indice + i * largura_barra, dados[i], largura_barra, label=f'Valores {i+1}')

# Configurações adicionais do gráfico
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras com Múltiplas Listas de Dados')
plt.xticks(indice + largura_total / (2 * num_listas), categorias)
plt.legend()

# Exibir o gráfico
plt.show()

