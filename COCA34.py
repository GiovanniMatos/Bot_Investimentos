import requests
from bs4 import BeautifulSoup
from plyer import notification

def valor_dolar():
    valor_compra = 46.20
    valor_venda = 47

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    request = requests.get("https://www.google.com/search?q=coca34&oq=coca34&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRg80gEINDIyMWoxajeoAgCwAgA&sourceid=chrome&ie=UTF-8",headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    valor_acao = soup.find("span", class_="IsqQVc NprOob wT3VGc")
    valor_texto = valor_acao.text
    valor_numero = float(valor_texto.replace(',', '.')) 
        
    if valor_numero <= valor_compra:
        print(f"Valor da ação: {valor_numero} --> [ Comprar ]")
        # Título e mensagem da notificação
        title = 'COMPRAR COCA34'
        message = 'Preço atual: R${}'.format(valor_numero)

        # Configuração da notificação
        notification.notify(
            title=title,
            message=message,
            app_name='Meu Aplicativo', 
            timeout=10  # Tempo para a notificação desaparecer
        )
    elif(valor_numero >= valor_venda):
        print(f"Valor da ação: {valor_numero} --> [ Vender ]")
        # Título e mensagem da notificação
        title = 'VENDER COCA34'
        message = 'Preço atual: R${}'.format(valor_numero)

        # Configuração da notificação
        notification.notify(
            title=title,
            message=message,
            app_name='Meu Aplicativo', 
            timeout=10  # Tempo em segundos para a notificação desaparecer
        )
    else:
        print(f"Valor da ação: R${valor_numero}")
