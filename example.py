import unittest, time, HtmlTestRunner
from selenium import webdriver
from termcolor import colored

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Python\\Testing\\chromedriver_win32\\chromedriver.exe")

    @classmethod 
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.driver.get("http://travel.agileway.net")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.find_element_by_link_text("Sign off").click()
               
    def test_case_1(self):  
        #ReturnWay Ticket correct dates     
        print("Test Case #1 Started *********************")
        self.assertEqual("Agile Travel", self.driver.title)
        self.driver.find_element_by_name("username").send_keys("agileway")
        self.driver.find_element_by_name("password").send_keys("testwise")
        self.driver.find_element_by_name("commit").click()
        self.assertTrue(self.driver.find_element_by_xpath("//*[text()='Signed in!']"))   
        print("Logged")   
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='return']").click()
        self.driver.find_element_by_xpath("//select[@name='fromPort']//option[text()='New York']").click()
        self.driver.find_element_by_xpath("//select[@name='toPort']//option[text()='Sydney']").click()
        print("Origin and Destination completed")
        self.driver.find_element_by_xpath("//select[@name='departDay']//option[text()='13']").click()
        self.driver.find_element_by_xpath("//select[@id='departMonth']//option[@value='122016']").click()
        self.driver.find_element_by_xpath("//select[@name='returnDay']//option[text()='20']").click()
        self.driver.find_element_by_xpath("//select[@id='returnMonth']//option[@value='122016']").click()
        self.driver.get_screenshot_as_file("TestCase1_1_ReturnWay.png")
        print("Dates completed")
        print("Access to Passenger Details")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Continue']").click()
        self.driver.find_element_by_name("passengerFirstName").send_keys("Daniel")
        self.driver.find_element_by_name("passengerLastName").send_keys("Perez")
        print("Passenger Details completed")
        self.driver.get_screenshot_as_file("TestCase1_2_PassengerDetails.png")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Next']").click()
        print("Access to Pay by Credit Card")
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='master']").click()
        self.driver.find_element_by_name("card_number").send_keys("1111222233334444")      
        self.driver.find_element_by_xpath("//select[@name='expiry_month']//option[@value='03']").click()
        self.driver.find_element_by_xpath("//select[@name='expiry_year']//option[@value='2018']").click()
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Pay now']").click()
        print("Confirmation completed")
        self.assertTrue(".//[@text='Confirmation']")
        self.driver.get_screenshot_as_file("TestCase1_3_PayByCreditCard.png")
        time.sleep(5)

    def test_case_2(self):  
        #ReturnWay Ticket incorrect dates
        print("Test Case #2 Started *******************")
        self.assertEqual("Agile Travel", self.driver.title)
        self.driver.find_element_by_name("username").send_keys("agileway")
        self.driver.find_element_by_name("password").send_keys("testwise")
        self.driver.find_element_by_name("commit").click()
        self.assertTrue(self.driver.find_element_by_xpath("//*[text()='Signed in!']"))   
        print("Logged")   
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='return']").click()
        self.driver.find_element_by_xpath("//select[@name='fromPort']//option[text()='New York']").click()
        self.driver.find_element_by_xpath("//select[@name='toPort']//option[text()='Sydney']").click()
        print("Origin and Destination completed")
        self.driver.find_element_by_xpath("//select[@name='departDay']//option[text()='03']").click()
        self.driver.find_element_by_xpath("//select[@id='departMonth']//option[@value='122016']").click()
        self.driver.find_element_by_xpath("//select[@name='returnDay']//option[text()='20']").click()
        self.driver.find_element_by_xpath("//select[@id='returnMonth']//option[@value='012016']").click()
        self.driver.get_screenshot_as_file("TestCase2_1_ReturnWay.png")
        print("Dates completed")
        print("Access to Passenger Details")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Continue']").click()
        self.driver.find_element_by_name("passengerFirstName").send_keys("Daniel")
        self.driver.find_element_by_name("passengerLastName").send_keys("Perez")
        print("Passenger Details completed")
        self.driver.get_screenshot_as_file("TestCase2_2_PassengerDetails.png")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Next']").click()
        print("Access to Pay by Credit Card")
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='master']").click()
        self.driver.find_element_by_name("card_number").send_keys("1111222233334444")      
        self.driver.find_element_by_xpath("//select[@name='expiry_month']//option[@value='03']").click()
        self.driver.find_element_by_xpath("//select[@name='expiry_year']//option[@value='2018']").click()
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Pay now']").click()
        print("Confirmation completed")
        self.driver.get_screenshot_as_file("TestCase2_3_PayByCreditCard.png")
        time.sleep(5)

    def test_case_3(self):  
        #OneWay Ticket incorrect dates
        print("Test Case #3 Started ********************")
        self.assertEqual("Agile Travel", self.driver.title)
        self.driver.find_element_by_name("username").send_keys("agileway")
        self.driver.find_element_by_name("password").send_keys("testwise")
        self.driver.find_element_by_name("commit").click()
        self.assertTrue(self.driver.find_element_by_xpath("//*[text()='Signed in!']"))   
        print("Logged")   
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='oneway']").click()
        self.driver.find_element_by_xpath("//select[@name='fromPort']//option[text()='New York']").click()
        self.driver.find_element_by_xpath("//select[@name='toPort']//option[text()='Sydney']").click()
        print("Origin and Destination completed")
        self.driver.find_element_by_xpath("//select[@name='departDay']//option[text()='13']").click()
        self.driver.find_element_by_xpath("//select[@id='departMonth']//option[@value='122016']").click()
        #self.driver.find_element_by_xpath("//select[@name='returnDay']//option[text()='20']").click()
        #self.driver.find_element_by_xpath("//select[@id='returnMonth']//option[@value='012016']").click()
        self.driver.get_screenshot_as_file("TestCase3_1_OneWay.png")
        print("Dates completed")
        print("Access to Passenger Details")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Continue']").click()
        self.driver.find_element_by_name("passengerFirstName").send_keys("Daniel")
        self.driver.find_element_by_name("passengerLastName").send_keys("Perez")
        print("Passenger Details completed")
        self.driver.get_screenshot_as_file("TestCase3_2_PassengerDetails.png")
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Next']").click()
        print("Access to Pay by Credit Card")
        self.driver.find_element_by_xpath(".//input[@type='radio' and @value='master']").click()
        self.driver.find_element_by_name("card_number").send_keys("1111222233334444")      
        self.driver.find_element_by_xpath("//select[@name='expiry_month']//option[@value='03']").click()
        self.driver.find_element_by_xpath("//select[@name='expiry_year']//option[@value='2018']").click()
        self.driver.find_element_by_xpath(".//input[@type='submit' and @value='Pay now']").click()
        print(colored('Confirmation Completed!','white','on_yellow'))
        self.assertTrue(".//[@text='Confirmation']")
        self.driver.get_screenshot_as_file("TestCase3_3_PayByCreditCard.png")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Python/Testing/Reports"))