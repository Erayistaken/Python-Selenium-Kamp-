from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class test_case:
    def test_case1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        loginBtn = driver.find_element(By.ID,"login-button")
        login.click()

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Kullanıcı adı ve şifre alanı boş geçilmiştir! {testResult}")



      

    def test_case2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")   

        input=driver.find_element(By.ID,"user-name")
        input.send_keys("1")

        loginBtn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Şifre alanı boş geçilmiştir! {test_Result}")





    def test_case3(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/") 

         inputUsername = driver.find_element(By.ID, "user-name")
         inputUsername.send_keys("locked_out_user")
         
         inputPassword = driver.find_element(By.ID, "password")
         inputPassword.send_keys("secret_sauce")

         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()

         errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
         print(f"Test sonucu : {testResult}" )




    def test_case4(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/") 

         loginBtn=driver.find_element(By.ID,"login-button")
         loginBtn.click()
         Button=driver.find_element(By.CLASS_NAME,"error-button")
         Button.click()




    def test_case5(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/") 

         inputUsername =  driver.find_element(By.ID, "user-name")
         inputPassword = driver.find_element(By.ID,"password")
         inputUsername.send_keys("standard_user")
         inputPassword.send_keys("secret_sauce")

         loginBtn =  driver.find_element(By.ID, "login-button")
         loginBtn.click()
         driver.get("https://www.saucedemo.com/inventory.html")




    def test_case6(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/") 

        inputUsername =  driver.find_element(By.ID, "user-name")
        inputPassword = driver.find_element(By.ID,"password")
        inputUsername.send_keys("standard_user")
        inputPassword.send_keys("secret_sauce")

        loginBtn =  driver.find_element(By.ID, "login-button")
        loginBtn.click()

        item = driver.find_elements(By.CLASS_NAME,"inventory_item")
        totalitem = (f"Toplam ürün sayısı: {len(item)}")
        print(totalitem)

        sleep(100000000)








testClass = test_case()
testClass.test_case1()
testClass.test_case2()
testClass.test_case3()
testClass.test_case4()
testClass.test_case5()
testClass.test_case6()

    
     



        

      

         


