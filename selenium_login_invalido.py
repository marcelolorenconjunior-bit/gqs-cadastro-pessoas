from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
try:
    driver.get('https://google.com')
    wait = WebDriverWait(driver, 10)
    busca = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    busca.send_keys('Gestao de Qualidade UTFPR Marcelo')
    busca.submit()
    wait.until(EC.url_contains('search'))
    print('CT-002 APROVADO POR MARCELO JUNIOR: Google carregou com sucesso!')
finally:
    driver.quit()
