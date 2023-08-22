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

    def make_query(self, query):
        search_bar = self.get_element_name("q")

        search_bar.click()
        search_bar.send_keys(query)

        ask_button = self.get_element_name( "btnK")

        ask_button.click()

        self.verify_title(f"{query} - Pesquisa Google")
        ijj_result = self.get_element_xpath("/html/body/div[6]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/a/h3")
        ijj_result.click()
        self.verify_title("Instituto Joga Junto")
        return 





    def form_section(self, name, mail, text):
        nome = self.get_element_name("nome")
        nome.send_keys(name)
        email = self.get_element_name("email")
        email.send_keys(mail)
        body = self.get_element_name("body")
        body.send_keys(text)


        assunto = self.get_element_name("assunto")

        select = Select(assunto)

        select.select_by_visible_text("Me inscrever em um curso")

        body.submit()
        return


    def browser_quit(self):
        self.navegador.quit()
        return


test = Test_case()
test.open_browser()
test.make_query("Instituto joga junto")
nomes = ["Matheus", "Michelle", "Mariana"]

# for nome in nomes:

#     test.form_section(nome, "matheus@matheusfsefasefsaef.com", "Texto teste")

sleep(3)
test.browser_quit()

