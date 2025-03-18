import time
from captura_tela import capturar_tela
from processamento_imagem import processar_imagem
from analise_tendencia import detectar_tendencia
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def executar_bot():
    """
    Executa a automação continuamente para monitorar o mercado.
    """
    # Configurações do Selenium para o Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximiza a janela
    chrome_options.add_argument("--disable-extensions")  # Desabilita extensões

    # Inicia o navegador Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://iqoption.com")  # Abre o site do IQ Option

    # Aguarda o carregamento da página (ajuste o tempo conforme necessário)
    time.sleep(5)

    # Loop de automação
    while True:
        print("\n🔍 Capturando tela...")
        img = capturar_tela()

        print("📊 Processando imagem...")
        _, contornos = processar_imagem(img)

        print("📈 Analisando tendência...")
        resultado = detectar_tendencia(contornos)

        print(f"📢 Sinal: {resultado}")

        # A automação pode interagir com a página do IQ Option aqui, se necessário
        # Por exemplo, para clicar em um botão ou coletar dados:
        # driver.find_element(By.XPATH, 'seu_xpath_aqui').click()

        time.sleep(5)  # Tempo entre análises

    # Fechar o navegador ao fim do script
    driver.quit()

if __name__ == "__main__":
    executar_bot()
