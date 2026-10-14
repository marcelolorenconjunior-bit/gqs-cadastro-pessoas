"""CT-001: Autenticacao com credenciais validas por Marcelo Lorencon Junior."""
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
    senha.send_keys("secret_sauce")
    
   
    botao = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    botao.click()
    
    
    wait.until(EC.url_contains("/inventory.html"))
    assert "inventory.html" in driver.current_url
    
    print("CT-001 APROVADO POR MARCELO JUNIOR: Login realizado com sucesso no Swag Labs!")

finally:
    driver.quit()
