"""CT-002: Autenticacao com credenciais invalidas por Marcelo Lorencon Junior."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("https://saucedemo.com")
    wait = WebDriverWait(driver, 10)
    
    usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    usuario.send_keys("standard_user")
    
    senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    senha.send_keys("senha_errada_123")  # Senha incorreta de propósito
    
    botao = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    botao.click()
    
    # VALIDAÇÃO DE GQS: Captura a mensagem de erro que aparece na tela vermelha
    elemento_erro = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    mensagem_erro = elemento_erro.text
    
    # Garante que a palavra "Password do not match" está no aviso de erro
    assert "password do not match" in mensagem_erro.lower()
    
    print("CT-002 APROVADO POR MARCELO JUNIOR:", mensagem_erro.strip())

finally:
    driver.quit()
