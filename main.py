#3th party
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#python
from time import sleep


def get_title_verify(title):
    assert title in browser.title
    print("Título verificado: " + title)
    return 

def get_element_name(name):
    tag_name = browser.find_element(By.NAME, name)
    print(f"O elemento {name} foi selecionado")
    return tag_name


def get_element_xpath(xpath):
    tag_xpath = browser.find_element(By.XPATH,xpath)
    print("o xpath foi verificado")
    return tag_xpath



# Crirar instância do navegador
browser = Firefox()

# Navegar até o site
browser.get("https://google.com")

#Econtrar a barra de pesquisa ( clicar, mandar o nome do ijj e mandar pesquisa)
barra_de_pesquisa = get_element_name("q")
barra_de_pesquisa.click
barra_de_pesquisa.send_keys('Instituto Joga Junto')
barra_de_pesquisa.send_keys(Keys.ENTER)

# Primeira verificação: Titulo
sleep(5)

get_title_verify("Instituto Joga Junto - Pesquisa Google")


# Entrar na página do instituto Joga Junto

get_element_xpath("/html/body/div[6]/div/div[13]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/a").click()
get_title_verify("Instituto Joga Junto")

nome = get_element_name("nome").send_keys("Matheus")
email = get_element_name("email").send_keys("matheus.ramos@jogajuntoinstituto.org")
mensagem = get_element_name("body").send_keys("Teste com Selenium ")
select_element = get_element_name("assunto")
select = Select(select_element)

select.select_by_visible_text("Me inscrever em um curso")

get_element_xpath("/html/body/div[1]/div[2]/section[8]/div[1]/form/button").submit()
#Acessando elemento do select



sleep(5)
browser.quit()

