import requests
from bs4 import BeautifulSoup
from plyer import notification

def valor_taee4():
    valor_compra = 11.55
    valor_venda = 12.50

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    request = requests.get("https://www.google.com/search?q=taee4&sca_esv=579280459&rlz=1C1FKPE_pt-PTBR1078BR1078&sxsrf=AM9HkKldNgneD48Z8Tr4VCpxllYiAfPung%3A1699045782898&ei=lmFFZfevNprY1sQPk4qLiA0&ved=0ahUKEwj30uLi3qiCAxUarJUCHRPFAtEQ4dUDCBA&oq=taee4&gs_lp=Egxnd3Mtd2l6LXNlcnAiBXRhZWU0SABQAFgAcAB4AZABAJgBAKABAKoBALgBDMgBAOIDBBgAIEE&sclient=gws-wiz-serp",headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    valor_acao = soup.find("span", class_="IsqQVc NprOob wT3VGc")
    valor_texto = valor_acao.text
    valor_numero = float(valor_texto.replace(',', '.')) 
        
    if valor_numero <= valor_compra:
        print(f"Valor da ação: {valor_numero} --> [ Comprar ]")
        # Título e mensagem da notificação
        title = 'COMPRAR TAEE4'
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
        title = 'VENDER TAEE4'
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

