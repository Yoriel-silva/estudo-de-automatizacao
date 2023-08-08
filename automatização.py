import pyautogui
from time import sleep

# Passos manuais para realizar esse processo:
# 1 - Clicar e digitar meu usuario
pyautogui.click(954,543,duration=2)
pyautogui.write('jhonatan')
# 2 - clicar e digitar minha senha
pyautogui.click(954,577,duration=2)
pyautogui.write('123456')
# 3 - clicar em entrar
pyautogui.click(849,616,duration=2)
# 4 - extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
    #     1 - clicar e digitar produto
        pyautogui.click(630,523,duration=2)
        pyautogui.write(produto)
    #     2 - clicar e digitar quantidade
        pyautogui.click(620,558,duration=2)
        pyautogui.write(quantidade)
    #     3 - clicar e digitar preço
        pyautogui.click(618,595,duration=2)
        pyautogui.write(preco)
    #     4 - clicar em registrar
        pyautogui.click(507,793,duration=2)
        sleep(1)
        
