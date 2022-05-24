#Bibliotecas

from ast import Return
from selenium import webdriver
from turtle import window_width
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep

# Dados ultilizados no script


busca = 'Python'
xpathBotaoEntrar = '//*[@id="organic-div"]/form/div[3]/button'
xpathBotaoPesquisa = '//*[@id="global-nav-typeahead"]/input'
xpathFiltroVagas = '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button'


# abrir navegador 
navegador = webdriver.Chrome()
url = "https://www.linkedin.com/login/"
navegador.get(url)
main_window = navegador.maximize_window()

try:
    # Realizar login no linkedin
    login = navegador.find_element_by_id("username")
    login.send_keys('') 

    senha = navegador.find_element_by_id("password")
    senha.send_keys('') 

    # Clicar no botão de entrar
    botao_entrar = navegador.find_element_by_xpath(xpathBotaoEntrar)
    botao_entrar.click()

    # Clicar no botão de Pesquisa e fazer a pesquisa
    botao_pesquisar = navegador.find_element_by_xpath(xpathBotaoPesquisa)
    botao_pesquisar.click()
    botao_pesquisar.send_keys(busca)
    botao_pesquisar.send_keys(Keys.RETURN)
    sleep(3)

    # Clicar no Botão para filtrar apenas vagas
    filtro_vagas = navegador.find_element_by_xpath(xpathFiltroVagas)
    filtro_vagas.click()

    


    input('')

#caso execeda o tempo aparecera o print da dando tempo esgotado
except TimeoutException:
    print('Tempo esgotado.')





