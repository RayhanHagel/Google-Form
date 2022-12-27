from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random


class Spammer:
    def __init__(self, url):
        service_ = Service('./driver/chromedriver.exe')
        options_ = Options()
        options_.add_experimental_option("detach", True)
        options_.add_argument("--headless")
        options_.add_argument('--no-sandbox')
        options_.add_argument('--disable-gpu')
        options_.add_argument('start-maximized')
        options_.add_argument('disable-infobars')
        options_.add_argument("--disable-extensions")
        
        self.url = url
        self.number = 0
        
        self.driver = webdriver.Chrome(service=service_, options=options_)    
        self.driver.get(self.url)
        with open("Harry.txt", encoding="utf8") as f:
            self.text = f.read().split("\n")
                    

    def check_order(self):
        bullet_order, checkbox_order = [], []        
        box = self.driver.find_elements(By.CLASS_NAME, "geS5n")
        bullet_normal = self.driver.find_elements(By.CLASS_NAME, "oyXaNc")
        bullet_scaled = self.driver.find_elements(By.CLASS_NAME, "N9Qcwe")
        checkboxes = self.driver.find_elements(By.CLASS_NAME, "Y6Myld")
        
        for index in range(len(box)):
            text = box[index].text
            if text.find("*") != -1: text = text.split("\n*\n")[1]
            else: text = '\n'.join(text.split('\n')[1:])
            for i in bullet_normal:
                if text.find(i.text) != -1:
                    bullet_order.append(len(i.text.split('\n')))
                    bullet_normal.pop(0)
            for i in bullet_scaled:
                if text.find(i.text) != -1:
                    bullet_order.append(len(i.text.split('\n'))-2)
                    bullet_scaled.pop(0)
            for i in checkboxes:
                if text.find(i.text) != -1:
                    checkbox_order.append(len(i.text.split('\n')))
                    checkboxes.pop(0)
        self.bullet_order, self.checkbox_order = bullet_order, checkbox_order
    
    
    def click_bullet(self):
        bullet = self.driver.find_elements(By.CLASS_NAME, "d7L4fc.bJNwt.aomaEc.ECvBRb")
        for index in range(len(self.bullet_order)):
            randomized = random.randint(0, self.bullet_order[index]-1)
            bullet[randomized].click()
            for i in range(self.bullet_order[index]): bullet.pop(0)
            
    
    def click_checkbox(self):
        checkboxes = self.driver.find_elements(By.CLASS_NAME, "uHMk6b.fsHoPb")
        for index in range(len(self.checkbox_order)):
            amount = self.checkbox_order[index]-1
            rand_list = random.sample(checkboxes[0: amount], random.randint(1, amount))
            for i in rand_list: i.click()
            for i in range(self.checkbox_order[index]): checkboxes.pop(0)
    
    
    def type_text(self):
        text_inputs = self.driver.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
        for text in text_inputs: text.send_keys(self.text[random.randint(0, len(self.text)-1)])
    
        
    def next_button(self):
        next_button = self.driver.find_elements(By.CLASS_NAME, 'NPEfkd.RveJvd.snByac')
        print(len(next_button))
        if len(next_button) == 2: next_button[0].click()
        else: next_button[1].click()
    
    
    def resubmit(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "vHW8K")
            self.number += 1
            print(f"Finished doing submission No. {self.number}")
            self.driver.get(self.url)
        except:
            print("Loading up next section...")
        
        
    def main(self):
        while True:
            self.check_order()
            self.click_bullet()
            self.type_text()
            self.click_checkbox()
            self.next_button()
            self.resubmit()
            break
        
        
if __name__ == '__main__':
    Program = Spammer("")
    Program.main()
    