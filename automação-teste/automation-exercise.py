from playwright.sync_api import sync_playwright
import time

# --- SUA LISTA DE TESTE ---
# Como o site é de teste, vamos usar termos que ele reconheça na busca
lista_busca = ["800001", "800002", "123456"] 

with sync_playwright() as p:
    # 1. Configuração do Navegador
    navegador = p.chromium.launch(headless=False) # Queremos ver o navegador
    contexto = navegador.new_context()
    pagina = contexto.new_page()

    # 2. Vai para a página de Login do Banco de Teste
    pagina.goto("http://demo.testfire.net/login.jsp")

    print("\n" + "="*60)
    print(" NO NAVEGADOR: Faça o login manual.")
    print(" Usuário: admin  |  Senha: admin")
    print(" Depois de logar, NÃO PRECISA CLICAR EM NADA.")
    print(" Volte aqui no terminal e aperte ENTER.")
    print("="*60)
    
    input("\n--- Pressione ENTER para iniciar a busca automática dos CPFs ---")

    # 3. Início da Automação em Lote
    for item in lista_busca:
        print(f"🔍 Buscando registro: {item}")

        # No Altoro Mutual, após logar, o campo de busca fica no topo (ID 'query')
        # Se o seletor mudar na área logada, o Playwright avisará
        try:
            # Preenche o campo de busca
            pagina.fill("#query", item)
            
            # Aperta Enter para pesquisar
            pagina.press("#query", "Enter")

            # Espera a rede carregar o resultado
            pagina.wait_for_load_state("networkidle")

            # Simula a extração de um dado da página de resultado
            # Aqui pegamos o título ou uma mensagem confirmando a busca
            resultado = pagina.locator("h1").inner_text()
            print(f"✅ Resultado para {item}: {resultado}")

            # Pequena pausa para você ver acontecendo
            time.sleep(1.5)

            # Opcional: Se precisar voltar para a tela inicial de busca
            # pagina.goto("http://demo.testfire.net/bank/main.jsp")
            
        except Exception as e:
            print(f"❌ Erro ao buscar {item}: Campo não encontrado ou timeout.")

    print("\n" + "="*60)
    print("AUTOMAÇÃO FINALIZADA!")
    print("O navegador fechará em 5 segundos...")
    print("="*60)
    
    time.sleep(5)
    navegador.close()