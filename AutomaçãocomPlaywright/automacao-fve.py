from operator import index

from playwright.sync_api import sync_playwright #playwright
import time


# --- CONFIGURAÇÃO DA LISTA ---
lista_cpfs = ["2345678901",
        "888999111",
        "99887766",
        "99900011122",
        "44433322211",
        "1101101101",
        "2233445566",
        "8877766655",
        "11223344556",
        "5511332266",
        "22883377441"
]
# --- CONFIGURAÇÃO DA PLAYWRIGHT ---

with sync_playwright() as p: # o p é de playwright
    navegador = p.chromium.launch(
        headless=False, # headless = false mostra o navegador na tela
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )
    # Criamos um contexto com um User-Agent real
    contexto = navegador.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )
    pagina = contexto.new_page()

    pagina.goto("https://www.parceirosantander.com.br/spa-base/landing-page")

    #login email e senha
    pagina.fill('xpath=//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input', "AAA")# primeiro adiciona o seletor nessa caso o path depois o que quer colocar no campo.
    pagina.fill('xpath=//*[@id="uabb-password-field"]', "cpf")
    pagina.fill('xpath=//*[@id="uabb-password-field"]', "99999999999")

    pagina.locator('xpath=//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button').click() #clicar botão de login
    pagina.wait_for_load_state("networkidle") # espera a página carregar completamente (sem requisições pendentes) antes de continuar, garantindo que o login foi processado e a próxima página está pronta para interação.

    print("Automação finalizada com sucesso!")
    time.sleep(5)
    navegador.close()
