from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By






driver = webdriver.Chrome()

class Test_Sauce:
    def __init__(self):
     
     pass
        
    
    def site():
     
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(3)
    def sifre():
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        sleep(3)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        print(firstResult)
    def sade_kul_ad():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        sleep(1)
       
        driver.find_element(By.ID,"login-button").click()
        sleep(3)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        print(firstResult)
        
        
    def sade_tik():
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        print(firstResult)     
        sleep(3)

    def error_icon():
          
        errorBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorBtn.click()   
        print("error icon kapatıldı")
        sleep(3)
          
    def locked_out_user():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
       
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
     
        print(firstResult)
        sleep(3)
        
     
    def login():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("standard_user")
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(1)
        driver.find_element(By.ID,"login-button").click()
        
        sayi = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Sayı {len(sayi)} ")
        sleep(2)
        driver.close()

t=Test_Sauce
t.site()
t.sade_tik()
t.error_icon()
t.sifre()
t.sade_kul_ad()
t.locked_out_user()
t.login()