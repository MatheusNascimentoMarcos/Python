from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
navegador.find_element('xpath','//*[@id="input"]').send_keys("cotação dolar")
navegador.find_element('xpath','//*[@id="input"]').send_keys(Keys.ENTER)
algo =  navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
#.send_keys para escrever
#.click para clicar
#.get para pegar
#.get_attribute pegar algo (copiar algo)