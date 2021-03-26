from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal! Aqui quem fala é um bot de testes."
        self.grupos = ["Hackathon Sírio", "Tribo Quidauanus Raiz"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Hackathon Sírio " class="_35k-1 _1adfa _3-8er">Hackathon Sírio </span>
        # <div tabindex="-1" class="_2A8P4">
        # <span data-icon="send" class="">
        print("asdasdasd")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
