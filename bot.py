from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Inicializa o navegador Chrome
driver = webdriver.Chrome()

# Abre o WhatsApp Web
driver.get("http://web.whatsapp.com")



# Aguarda o usuário escanear o código QR manualmente
print("Por favor, escaneie o código QR para fazer login.")

try:
    while True:
        try:
            chat = driver.find_elements(By.XPATH,'//*[@id="pane-side"]/button/div/div[2]/div/div')
            if chat:
                print('carregou chat')
               # cnvs = driver.find_element(By.XPATH, '//span[@title="Rosilei"]').click()
                comando = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/span')
                comando_text = comando.text

                #desligar
                if comando_text.lower() == 'desligar':
                    print('Comando de desligamento detectado')
                    if os.name == 'posix':
                        os.system('sudo shutdown now')
                    else:
                        os.system('shutdown /s /f /t 0')

                    #abrir youtube
                if comando_text.lower() == 'google':
                    driver.get('https://google.com')

                
        except NoSuchElementException:
            time.sleep(1)  # espera 1 segundo antes de tentar novamente
        
                
        else:
            print('chat nao encontrado')
            time.sleep(1)

except Exception as e:
    print(f'Erro ao encontrar o chat: {e}')

# Fecha o navegador
time.sleep(5)
driver.quit()