import requests
from bs4 import BeautifulSoup
from plyer import notification

def valor_ggbr4():
    valor_compra = 21.60
    valor_venda = 26.30

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    request = requests.get("https://www.google.com/search?q=ggbr4&oq=ggbr4&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GJ0CGIoFMg4IABBFGCcYOxidAhiKBTIGCAEQRRhAMg0IAhAAGIMBGLEDGIAEMg0IAxAAGIMBGLEDGIAEMgcIBBAAGIAEMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg80gEIMTMwNGoxajeoAgCwAgA&sourceid=chrome&ie=UTF-8",headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    valor_acao = soup.find("span", class_="IsqQVc NprOob wT3VGc")
    valor_texto = valor_acao.text
    valor_numero = float(valor_texto.replace(',', '.')) 
        
    if valor_numero <= valor_compra:
        print(f"Valor da ação: {valor_numero} --> [ Comprar ]")
        # Título e mensagem da notificação
        title = 'COMPRAR GGBR4'
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
        title = 'VENDER GGBR4'
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
