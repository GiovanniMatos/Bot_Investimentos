import requests
from bs4 import BeautifulSoup
from plyer import notification

def valor_dolar():
    valor_compra = 4.9
    valor_venda = 5.5

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    request = requests.get("https://www.google.com/search?q=dolar+&sca_esv=578489342&sxsrf=AM9HkKlgNn5lciouNQkEsQcyxBPNiOP6FQ%3A1698845688943&ei=-FNCZfKXOYiK5OUPneWH-AY&ved=0ahUKEwjy88Su9aKCAxUIBbkGHZ3yAW8Q4dUDCBA&uact=5&oq=dolar+&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmRvbGFyIDIHECMYigUYJzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMggQABiABBixA0j2ClDiCFjiCHACeAGQAQCYAewBoAHsAaoBAzItMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhD4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp",headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    valor_acao = soup.find("span", class_="DFlfde SwHCTb")
    valor_texto = valor_acao.text
    valor_numero = float(valor_texto.replace(',', '.')) 
        
    if valor_numero <= valor_compra:
        print(f"Valor da ação: {valor_numero} --> [ Comprar ]")
        # Título e mensagem da notificação
        title = 'COMPRAR DÓLAR'
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
        title = 'VENDER DÓLAR'
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
