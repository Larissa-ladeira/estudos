import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- CONFIGURAÇÃO DA PLANILHA (Mantida igual) ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
cliente = gspread.authorize(creds)
planilha = cliente.open("Automação-Playwright").sheet1

# --- CONFIGURAÇÃO DO SELENIUM ---
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Mantém o navegador aberto se desejar

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abrir site
    driver.get("https://www.cursoemvideo.com/login/")
    driver.maximize_window()

    # O Selenium precisa de uma espera explícita para garantir que os elementos apareçam
    wait = WebDriverWait(driver, 20)

    # Login de email e senha (usando seus XPaths originais)
    email_field = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             '//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input')))
    email_field.send_keys("larissaladeira42@gmail.com")

    password_field = driver.find_element(By.XPATH, '//*[@id="uabb-password-field"]')
    password_field.send_keys("girlhell1")

    # Clicar botão de login
    login_btn = driver.find_element(By.XPATH,
                                    '//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button')
    login_btn.click()

    time.sleep(5)

    # Opções clicáveis
    # Clicar nos cursos disponíveis
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-283541"]/a'))).click()

    # Clicar no curso de python
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="post-283493"]/div/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[13]/div/div[5]/a/img'))).click()

    # Clicar no botão expandir
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ld-expand-button-26338"]/span[2]'))).click()

    # Clicar na primeira aula
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ld-table-list-item-26340"]/a/span'))).click()

    # Extrair título
    xpath_titulo = '//*[@id="ld-tab-content-26338"]/h2[1]'
    elemento_titulo = wait.until(EC.presence_of_element_located((By.XPATH, xpath_titulo)))
    titulo = elemento_titulo.text  # Equivalente ao inner_text

    time.sleep(5)

    # Mostrar alert no navegador (Execução de JavaScript)
    driver.execute_script(f"alert('Título copiado com sucesso: {titulo}')")
    time.sleep(2)  # Pausa para você ver o alerta antes de aceitar
    driver.switch_to.alert.accept()

    driver.execute_script("alert('Programa executado com sucesso!')")
    time.sleep(2)
    driver.switch_to.alert.accept()

    # Salvar na planilha google o titulo extraido
    planilha.insert_row(["", "", titulo], index=2)
    print(f"Sucesso! '{titulo}' foi adicionado à planilha.")

    time.sleep(15)

finally:
    # Fechar o navegador
    driver.quit()