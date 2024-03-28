import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render

def grafico_barras(request):
    categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
    dados = [[20, 35, 30], [25, 32, 34], [30, 23, 32]]

    fig, ax = plt.subplots()
    x = range(len(categorias))

    for i in range(len(dados)):
        ax.bar(x, dados[i], label=f'Dados {i+1}')

    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'grafico.html', {'graphic': graphic})



