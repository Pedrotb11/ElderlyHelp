from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ender: str= "rua aleatoriado bairro, Bairro"

navegador = webdriver.Chrome()
navegador.get("https://www.uber.com/br/pt-br/")

navegador.find_element(By.XPATH,'//*[@id="2"]/div/div/span').click()

navegador.find_element(By.XPATH,
    '//*[@id="animation-wrapper"]/section/div/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/input').send_keys(f"{ender}")