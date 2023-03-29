from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
from datetime import date
import pytest
#prefix => on ek test
#postfix
class Test_Update_Demo:
    # Her testten önce çağrılır
    def waitForElementVisible(self,locator,timeout=5):
           WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    # Her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    # setup -> test_demoFunc -> teardown    
    def test_demoFunc(self):
        print("hello")
        # 3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"

    def test_demo2(self):
        assert True

    # @pytest.mark.skip()
    def test_case(self):
        self.waitForElementVisible((By.ID, 'login-button'))

        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()

        self.waitForElementVisible(
            (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))

        errorMessage = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login.png")

        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username,password",[("hatalı","deneme") , ("1","1"), ("0","0")])
    def test_case2(self,username,password):

         self.waitForElementVisible((By.ID, "user-name"))
         usernameInput = self.driver.find_element(By.ID, "user-name")

         self.waitForElementVisible((By.ID, "password"),10)
         passwordInput = self.driver.find_element(By.ID, "password") 
        
         usernameInput.send_keys(username)
         passwordInput.send_keys(password)

         loginBtn = self.driver.find_element(By.ID, "login-button")
         loginBtn.click()

         self.waitForElementVisible(
            (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))
        
         errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
         self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
         assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    

    @pytest.mark.parametrize("username", [("standard_user")])
    def test_case3(self,username):
       self.waitForElementVisible((By.ID, 'user-name'))
       userInput = self.driver.find_element(By.ID, 'user-name')
       userInput.send_keys(username)

        #self.waitForElementVisible(By.ID, "password",5)
        #passwordInput = self.driver.find_element(By.ID, "password")
        #passwordInput.send_keys(password)

       self.waitForElementVisible((By.ID, 'login-button'))
       loginBtn = self.driver.find_element(By.ID, 'login-button')
       loginBtn.click()

       self.waitForElementVisible((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))
       errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")


       self.driver.save_screenshot(f"{self.folderPath}/test-null-password.png")
       assert errorMessage.text == "Epic sadface: Password is required"
        
    @pytest.mark.parametrize("username, password",[("locked_out_user","secret_sauce")])
    def test_case4(self,username,password):   
        self.waitForElementVisible((By.ID, 'user-name'))
        userInput = self.driver.find_element(By.ID, 'user-name')

        self.waitForElementVisible((By.ID, 'password'),2)
        passwordInput = self.driver.find_element(By.ID, 'password')

        userInput.send_keys(username)
        passwordInput.send_keys(password) 

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()   

        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-login.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        

    def test_case5(self):       
        loginBtn = self.driver.find_element(By.ID, "login-button")     
        loginBtn.click()      

        errorCloseIcon = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")   
        self.driver.save_screenshot(f"{self.folderPath}/test-error-icon.png") 
        errorCloseIcon.click()
        
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_case6(self,username,password):
        self.waitForElementVisible((By.ID, 'user-name'))
        userInput = self.driver.find_element(By.ID, 'user-name')
        self.waitForElementVisible((By.ID, 'password'),2)
        passwordInput = self.driver.find_element(By.ID, 'password')
        userInput.send_keys(username)
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID, "login-button")  
        loginBtn.click()
        self.driver.current_url == ("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-login-inventory-{username}-{password}.png")
 
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_case7(self,username,password): 
        self.waitForElementVisible((By.ID, 'user-name'))
        userInput = self.driver.find_element(By.ID, 'user-name')
        self.waitForElementVisible((By.ID, 'password'),1)
        passwordInput = self.driver.find_element(By.ID, 'password')
        userInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        lenProduct = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Lenght Product Result : {len(lenProduct)}")
        self.driver.save_screenshot(f"{self.folderPath}/test-all-product-{username}-{password}.png")
        
    
    

    def test_case8(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-shopping.png")
        
       


    def test_case9(self):
        
        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, 'user-name')
        self.waitForElementVisible((By.ID, 'password'),1)

        passwordInput = self.driver.find_element(By.ID, 'password')
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        
         # Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, 'standard_user')
        actions.send_keys_to_element(passwordInput, 'secret_sauce')
        actions.send_keys_to_element(loginBtn, Keys.ENTER)
        actions.perform()
        
        self.waitForElementVisible((By.CLASS_NAME, 'inventory_list'))
        loginBtn = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

        self.driver.save_screenshot(
            f"{self.folderPath}/test-valid-login.png")
   