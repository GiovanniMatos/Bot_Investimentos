import requests
from bs4 import BeautifulSoup
from plyer import notification


def valor_vale3():
    valor_compra = 65
    valor_venda = 70

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    request = requests.get("https://www.google.com/search?q=vale3&oq=vale&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GJ0CGIoFMg4IABBFGCcYOxidAhiKBTITCAEQLhiDARjHARixAxjRAxiABDIGCAIQRRhAMg0IAxAuGIMBGLEDGIAEMg0IBBAAGIMBGLEDGIAEMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg80gEIMTA0NGoxajmoAgCwAgA&sourceid=chrome&ie=UTF-8",headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    valor_acao = soup.find("span", class_="IsqQVc NprOob wT3VGc")
    valor_texto = valor_acao.text
    valor_numero = float(valor_texto.replace(',', '.')) 
        
    if valor_numero <= valor_compra:
        print(f"Valor da ação: {valor_numero} --> [ Comprar ]")
        # Título e mensagem da notificação
        title = 'COMPRAR VALE3'
        message = 'Preço atual: R${}'.format(valor_numero)

        notification.notify(
            title=title,
            message=message,
            app_name='Meu Aplicativo',  
            timeout=10  # Tempo para a notificação desaparecer
        )
    elif(valor_numero >= valor_venda):
        print(f"Valor da ação: {valor_numero} --> [ Vender ]")
        title = 'VENDER VALE3'
        message = 'Preço atual: R${}'.format(valor_numero)

        notification.notify(
            title=title,
            message=message,
            app_name='Meu Aplicativo', 
            timeout=10  # Tempo em segundos para a notificação desaparecer
        )
    else:
        print(f"Valor da ação: R${valor_numero}")

