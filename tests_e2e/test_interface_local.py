import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

# Delay para observação entre as ações.
DELAY = 2

@pytest.fixture(scope="module")
def driver():
    """
    Configura e inicializa o WebDriver do Chrome, navega para a URL
    do frontend e o disponibiliza para os testes. No final, encerra o driver.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    driver.get("https://locadora-frontend.onrender.com/") 
    
    yield driver
    
    print("\nTodos os testes foram concluídos. Aguardando 5 segundos antes de fechar o navegador...")
    time.sleep(5)
    driver.quit()

class TestLocadoraFrontend:
    """
    Agrupa todos os testes de ponta a ponta para o frontend da locadora.
    """

    def test_deve_navegar_entre_secoes(self, driver):
        """
        Verifica se a navegação entre as seções principais funciona.
        """
        wait = WebDriverWait(driver, 10)
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='veiculos-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Gerenciar Veículos')]")))
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='reservas-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Gerenciar Reservas')]")))
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='extras-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Relatórios')]")))
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='clientes-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Gerenciar Clientes')]")))

    def test_fluxo_crud_cliente(self, driver):
        """
        Testa o fluxo completo de CRUD (Criar, Ler, Atualizar, Excluir) para um cliente.
        """
        wait = WebDriverWait(driver, 10)
        timestamp = int(time.time())
        nome_cliente = f"Cliente Teste {timestamp}"
        email_cliente = f"teste{timestamp}@example.com"
        cpf_cliente = f"{timestamp % 10000000000:011}"
        telefone_editado = "61999998888"

        # --- CRIAR ---
        time.sleep(DELAY)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add[data-type='cliente']"))).click()
        
        wait.until(EC.visibility_of_element_located((By.ID, "cliente-nome")))
        time.sleep(DELAY)
        driver.find_element(By.ID, "cliente-nome").send_keys(nome_cliente)
        time.sleep(DELAY)
        driver.find_element(By.ID, "cliente-email").send_keys(email_cliente)
        time.sleep(DELAY)
        driver.find_element(By.ID, "cliente-cpf").send_keys(cpf_cliente)
        time.sleep(DELAY)
        driver.find_element(By.ID, "endereco-rua").send_keys("Rua Teste")
        time.sleep(DELAY)
        driver.find_element(By.ID, "endereco-cidade").send_keys("Brasília")
        time.sleep(DELAY)
        driver.find_element(By.ID, "endereco-estado").send_keys("DF")
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-cliente .btn-save").click()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()

        # --- LER (Verificar Criação) ---
        xpath_cliente = f"//td[text()='{nome_cliente}']"
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_cliente)))

        # --- ATUALIZAR ---
        time.sleep(DELAY)
        btn_editar = driver.find_element(By.XPATH, f"{xpath_cliente}/following-sibling::td/button[contains(@class, 'btn-edit')]")
        btn_editar.click()

        campo_telefone = wait.until(EC.visibility_of_element_located((By.ID, "cliente-telefone")))
        time.sleep(DELAY)
        campo_telefone.clear()
        time.sleep(DELAY)
        campo_telefone.send_keys(telefone_editado)

        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-cliente .btn-save").click()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()

        xpath_telefone_editado = f"//td[text()='{nome_cliente}']/following-sibling::td[text()='{telefone_editado}']"
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_telefone_editado)))
        
        # --- EXCLUIR ---
        time.sleep(DELAY)
        btn_excluir = driver.find_element(By.XPATH, f"{xpath_cliente}/following-sibling::td/button[contains(@class, 'btn-delete')]")
        btn_excluir.click()

        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()

        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_cliente)))

    def test_fluxo_crud_veiculo(self, driver):
        """
        Testa o fluxo de Criar e Excluir para um veículo.
        """
        wait = WebDriverWait(driver, 10)
        timestamp = int(time.time())
        placa_veiculo = f"TES{timestamp % 1000:04}"
        modelo_veiculo = "Carro de Teste"
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='veiculos-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Gerenciar Veículos')]")))
        
        # --- CRIAR ---
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "button.btn-add[data-type='veiculo']").click()
        
        wait.until(EC.visibility_of_element_located((By.ID, "veiculo-placa")))
        time.sleep(DELAY)
        driver.find_element(By.ID, "veiculo-placa").send_keys(placa_veiculo)
        time.sleep(DELAY)
        driver.find_element(By.ID, "veiculo-modelo").send_keys(modelo_veiculo)
        time.sleep(DELAY)
        driver.find_element(By.ID, "veiculo-diaria").send_keys("150.50")
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-veiculo .btn-save").click()

        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()

        # --- LER e EXCLUIR ---
        xpath_veiculo = f"//td[text()='{placa_veiculo}']"
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_veiculo)))

        time.sleep(DELAY)
        driver.find_element(By.XPATH, f"{xpath_veiculo}/following-sibling::td/button[contains(@class, 'btn-delete')]").click()

        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()
        
        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_veiculo)))

    def test_fluxo_crud_reserva(self, driver):
        """
        Testa o fluxo completo de CRUD para uma Reserva usando dados existentes.
        """
        wait = WebDriverWait(driver, 10)

        # --- NAVEGAÇÃO ---
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='reservas-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Gerenciar Reservas')]")))

        # --- CRIAR RESERVA ---
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "button.btn-add[data-type='reserva']").click()
        
        modal_reserva = wait.until(EC.visibility_of_element_located((By.ID, "form-reserva")))
        
        # Seleciona o primeiro cliente e veículo da lista
        time.sleep(DELAY)
        Select(modal_reserva.find_element(By.ID, "reserva-cliente")).select_by_index(1)
        
        time.sleep(DELAY)
        Select(modal_reserva.find_element(By.ID, "reserva-veiculo")).select_by_index(1)
        
        # Define datas para a reserva dentro do ano de 2025
        data_inicio = "2025-12-01"
        data_fim = "2025-12-05"
        data_fim_editada = "2025-12-07"
        
        # Usa execute_script para definir a data de forma confiável
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", driver.find_element(By.ID, "reserva-inicio"), data_inicio)
        
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", driver.find_element(By.ID, "reserva-fim"), data_fim)

        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-reserva .btn-save").click()
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        
        # --- LER (Verificar Criação) ---
        data_inicio_formatada = datetime.strptime(data_inicio, '%Y-%m-%d').strftime('%d/%m/%Y')
        xpath_reserva = f"//td[contains(text(), '{data_inicio_formatada}')]/ancestor::tr"
        linha_reserva = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_reserva)))
        
        # --- ATUALIZAR RESERVA ---
        time.sleep(DELAY)
        linha_reserva.find_element(By.CLASS_NAME, "btn-edit").click()
        
        modal_edit = wait.until(EC.visibility_of_element_located((By.ID, "form-reserva")))
        
        # Usa execute_script para definir a data de forma confiável
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", driver.find_element(By.ID, "reserva-fim"), data_fim_editada)
        
        time.sleep(DELAY)
        modal_edit.find_element(By.CSS_SELECTOR, ".btn-save").click()
        alert = wait.until(EC.alert_is_present())
        alert.accept()

        # Verificar atualização
        data_fim_formatada_verificacao = datetime.strptime(data_fim_editada, '%Y-%m-%d').strftime('%d/%m/%Y')
        wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath_reserva), data_fim_formatada_verificacao))
        
        # --- EXCLUIR RESERVA ---
        time.sleep(DELAY)
        driver.find_element(By.XPATH, xpath_reserva).find_element(By.CLASS_NAME, "btn-delete").click()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()
        
        alert = wait.until(EC.alert_is_present())
        time.sleep(DELAY)
        alert.accept()
        
        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_reserva)))

    def test_extras_busca_veiculos_disponiveis(self, driver):
        """
        Testa a funcionalidade de busca de veículos disponíveis na seção 'Extras'.
        """
        wait = WebDriverWait(driver, 10)
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='extras-section']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Buscar Veículos Disponíveis')]")))

        data_inicio = "2025-08-01"
        data_fim = "2025-08-05"
        
        campo_inicio = driver.find_element(By.ID, "busca-inicio")
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", campo_inicio, data_inicio)
        
        campo_fim = driver.find_element(By.ID, "busca-fim")
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", campo_fim, data_fim)
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-busca-veiculos .btn-action").click()
        
        resultado_card = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#busca-veiculos-result-container > .result-card")))
        assert "Resultado da Busca" in resultado_card.text
        print("\nSUCESSO: Formulário de busca de veículos foi testado e o resultado apareceu.")

    def test_extras_relatorio_faturamento(self, driver):
        """
        Testa a funcionalidade de geração de relatório de faturamento.
        """
        wait = WebDriverWait(driver, 10)
        
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, ".nav-link[data-section='extras-section']").click()
        
        wait.until(EC.visibility_of_element_located((By.ID, "form-relatorio-faturamento")))

        data_inicio_relatorio = "2025-09-01"
        data_fim_relatorio = "2025-09-30"
        
        campo_inicio_relatorio = driver.find_element(By.ID, "relatorio-inicio")
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", campo_inicio_relatorio, data_inicio_relatorio)

        campo_fim_relatorio = driver.find_element(By.ID, "relatorio-fim")
        time.sleep(DELAY)
        driver.execute_script("arguments[0].value = arguments[1];", campo_fim_relatorio, data_fim_relatorio)

        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "#form-relatorio-faturamento .btn-action").click()

        resultado_card = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#relatorio-faturamento-result-container > .result-card")))
        
        assert "Resultado: Relatório de Faturamento" in resultado_card.text
        assert "Faturamento Total" in resultado_card.text
        
        print("\nSUCESSO: Formulário de relatório de faturamento foi testado e o resultado apareceu.")