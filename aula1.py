from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from time import sleep

class Test_case():
    def __init__(self):
        
        self.navegador = webdriver.Firefox()

    def get_element_name(self, name):
        print(f"Elemento selecionado, com nome: {name}")
        return self.navegador.find_element(By.NAME, name)

    def get_element_xpath(self, name):
        print(f"Elemento selecionado, com nome: {name}")
        return self.navegador.find_element(By.XPATH, name)
        
        
    def verify_title(self, title):
        sleep(3)
        assert title in self.navegador.title
        print(f"O título {title} foi validado")
        return



    def open_browser(self):

        self.navegador.get("https://google.com")

    def make_query(self):
        search_bar = self.get_element_name("q")

        search_bar.click()
        search_bar.send_keys("Instituto joga junto")

        ask_button = self.get_element_name( "btnK")

        ask_button.click()

        self.verify_title("Instituto joga junto - Pesquisa Google")
        ijj_result = self.get_element_xpath("/html/body/div[6]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/a/h3")
        ijj_result.click()
        self.verify_title("Instituto Joga Junto")
        ...






        def form_section(self, name, mail, subject, text):
            nome = self.get_element_name("nome")
            nome.send_keys(name)
            email = self.get_element_name("email")
            email.send_keys("matheus.ramos@jogajuntoinstituto.org")
            body = self.get_element_name("body")
            body.send_keys("Teste Selenium - Aula 1")


            assunto = self.get_element_name("assunto")

            select = Select(assunto)

            select.select_by_visible_text("Me inscrever em um curso")

            body.submit()


            def browser_quit():
                self.navegador.quit()
