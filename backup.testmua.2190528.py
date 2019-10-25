import unittest, time, HtmlTestRunner, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MuaTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Python\\Testing\\chromedriver_win32\\chromedriver.exe")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.driver.get("http://134.209.63.241:8080/mua2/")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver = None
    
    def testcase01_create_new_category(self):
        try:
            print ("***** Test Case 01 - Create new Category *****")
            #self.driver.get("http://134.209.63.241:8080/mua2/categories")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[2]//a[1]"))).click() 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='btn btn-primary']"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"nombre"))).send_keys("Automatic Category")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit' and @class='mt-2 btn btn-primary']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase01_01_NewCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase02_create_new_tag(self):
        try:
            print ("***** Test Case 02 - Create New Tags *****")
            #self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[4]//a[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-tags[@class='ng-star-inserted']//div[1]//div[1]//div[1]//button[1]"))).click() 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"nombre"))).send_keys("2018") 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"descripcion"))).send_keys("Year 2018") 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-tags[@class='ng-star-inserted']//div[1]//div[1]//div[1]//button[1]"))).click() 
            self.driver.get_screenshot_as_file("screenshots/TestCase02_01_Tags.png") 
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase03_create_new_post(self):
        try:
            print ("***** Test Case 03 - Create new Post attaching PNG image *****")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[3]//a[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//input[1]"))).send_keys("New Post 5")  
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//select[1]//option[3]"))).click() 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//div[2]//div[1]//input"))).send_keys("Asia")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//div[2]//div[1]//input"))).send_keys(Keys.ENTER)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//div[2]//div[1]//input"))).send_keys("China")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//div[2]//div[1]//input"))).send_keys(Keys.ENTER)           
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-post[@class='ng-star-inserted']//button[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"avatar"))).send_keys("C:\\Repository\\automatedtest\\screenshots\\jpg.jpg")
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")     
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit' and @class='btn btn-primary my-2']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase03_01_OpenPost.png")  
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase04_update_post(self):
        try:
            print ("***** Test Case 04 - Edit Post, Update General Information, add new image *****")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//select[@ng-model='busqueda.categoria']//option[@value='Automatic Category']"))).click() 
            self.driver.get_screenshot_as_file("screenshots/TestCase04_00_FilterPost.png")
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Automatic Tag')]"))).click()            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='container']//div[1]//div[2]//div[4]//a[2]"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase04_01_GoPost.png")
            self.driver.find_element_by_id("titulo").clear()
            self.driver.find_element_by_id("titulo").send_keys("Update Automatic Post")
            self.driver.find_element_by_id("descripcion").clear()
            self.driver.find_element_by_id("descripcion").send_keys("Morbi volutpat sapien sollicitudin suscipit venenatis. Nulla posuere orci ac vulputate sollicitudin. Cras eu fringilla sem, scelerisque bibendum libero. Aenean at magna dolor. Nullam semper posuere neque ac scelerisque. Aenean leo lectus, lacinia sit amet purus vel, feugiat pulvinar nisl. Nulla dictum porta odio, quis molestie orci molestie vitae. Maecenas interdum dolor eget purus pharetra egestas. Aliquam sed aliquam turpis. Donec ac quam quis elit venenatis maximus. Maecenas vitae nunc id velit pulvinar mattis at non diam. Morbi porta neque sed accumsan semper.")            
            self.driver.get_screenshot_as_file("screenshots/TestCase04_02_EditPost.png")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='container']//div[1]//div[1]//div[3]//div[1]//div[1]"))).click()
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\hqdefault.jpg")
            self.driver.get_screenshot_as_file("screenshots/TestCase04_03_OpenImage.png")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='submit' and @value='Subir imagen']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase04_04_SavePost.png")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='row']//a[1]//button[@class='btn btn-primary']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase04_05_HomePage.png")        
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase05_view_images(self):
        try:
            print("***** Test Case 05 - Search posts and view images *****")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//select[@id='wgtmsr']//option[@value='Moda Mexico']"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-root[1]//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='mat-calendar-table']//tbody[1]//tr[3]//td[4]//div[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//mat-form-field[2]//div[1]//div[1]//div[2]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='mat-calendar-table']//tbody[1]//tr[5]//td[3]//div[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//mat-form-field[2]//div[1]//div[1]//div[2]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='mat-calendar-table']//tbody[1]//tr[5]//td[2]//div[1]"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@role='combobox']"))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//ng-dropdown-panel[@class='ng-dropdown-panel ng-select-multiple ng-star-inserted ng-select-bottom']//div[1]//div[2]//div[1]"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase05_01_SearchCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True 

    def testcase06_change_default_image(self):
        try:
            print("***** Test Case 06 - Change Default Image in Post *****")            
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Automatic Category']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[4]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase06_01_ShowPost.png") 
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='container']//div[1]//div[1]//div[2]//div[2]//i[1]"))).click()            
            self.driver.get_screenshot_as_file("screenshots/TestCase06_02_ChangeDefault.png")            
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//button[@class='swal-button swal-button--confirm swal-button--danger']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase06_03_ConfirmChangeDefault.png")            
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//button[@class='swal-button swal-button--confirm']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase06_04_CheckCurrentImages.png")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='row']//a[1]//button[@class='btn btn-primary']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase06_05_HomePage.png")
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    def testcase07_delete_post(self):
        try:
            #By the moment this feature is unable
            print("***** Test Case 07 - Delete Posts *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Automatic Category']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase07_01_ViewPost.png")
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[4]//a[3]//i[1]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase07_02_ConfirmDeletePost.png")            
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[2]//div[2]//button[1]"))).click()            
            self.driver.get_screenshot_as_file("screenshots/TestCase07_03_DeletePost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase08_update_category(self):
        try:
            print("***** Test Case 08 - Update Categories *****")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[2]//a[1]"))).click() 
            self.driver.get_screenshot_as_file("screenshots/TestCase08_01_AccessCategories.png") 
            time.sleep(5) 
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):     
                    if (WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-striped']//tbody//tr[%d]//td[2]" % (row)))).get_attribute("innerHTML") == 'new category'):
                        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-striped']//tbody//tr[%d]//td[3]//i[1]" % (row)))).click() 
                        self.driver.find_element_by_xpath("//div[@class='ng-star-inserted']//input[2]").clear()
                        self.driver.find_element_by_xpath("//div[@class='ng-star-inserted']//input[2]").send_keys("Automatic Category")                       
                        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='ng-star-inserted']//div[1]//button[1]"))).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase08_02_EditCategory.png")
            self.driver.get("http://134.209.63.241:8080/mua2/")
            self.driver.get_screenshot_as_file("screenshots/TestCase08_03_HomePage.png")                   
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase09_delete_category(self):
        try:
            #By the moment this feature is blocked, we aren't not able to delete assigned Post
            print("***** Test Case 09 - Delete Categories *****")
            #self.driver.get("http://134.209.63.241:8080/mua/#!/ejemplos")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[2]//a[1]"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase09_01_AccessCategories.png") 
            time.sleep(5) 
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):
                       if (WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-striped']//tbody//tr[%d]//td[2]" % (row)))).get_attribute("innerHTML") == 'xxx'):         
                           WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-striped']//tbody//tr[%d]//td[4]//i[1]" % (row)))).click() 
                           self.driver.get_screenshot_as_file("screenshots/TestCase09_02_DeleteCategory.png")    
                           WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-dialog//div[1]//div[1]//button[1]"))).click() 
                           self.driver.get_screenshot_as_file("screenshots/TestCase09_03_ConfirmDeleteCategory.png")                                                                                
            self.driver.get("http://134.209.63.241:8080/mua2/")
            self.driver.get_screenshot_as_file("screenshots/TestCase09_03_HomePage.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase10_edit_tag(self):
        try:
            print("***** Test Case 10 - Edit Tag *****")
            #self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[4]//a[1]"))).click()
            time.sleep(5)
            #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase10_01_TagsRows.png") 
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr"))
            for row in range(rows+1):
                if (row>1):                
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Tag1'):   
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[4]//i[1]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase10_02_AccessEditTagsPage.png") 
                        self.driver.find_element_by_name("nombre").clear()
                        self.driver.find_element_by_name("nombre").send_keys("New Tag1")
                        self.driver.find_element_by_name("descripcion").clear()
                        self.driver.find_element_by_name("descripcion").send_keys("New Tag1")                       
                        WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//app-tags[@class='ng-star-inserted']//div[1]//div[1]//div[1]//button[1]"))).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase10_03_TagsUpdated.png")                        
                        '''WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//button[@class='swal-button swal-button--confirm']"))).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase10_04_TagsExit.png")'''
            #self.driver.get("http://134.209.63.241:8080/mua/#!")
            self.driver.get("http://134.209.63.241:8080/mua2/")
            self.driver.get_screenshot_as_file("screenshots/TestCase10_05_HomePage.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase11_delete_tag(self):
        try:
            print("***** Test Case 11 - Delete Tag *****")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbarNav']//ul//li[4]//a[1]"))).click()
            time.sleep(5)
            #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase10_01_TagsRows.png") 
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr"))
            for row in range(rows+1):
                if (row>1):                
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'tAG0'):   
                        print("Test")
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[5]//i[1]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase11_02_AccessEditTagsPage.png")                         
                        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//app-dialog[@class='ng-star-inserted']//div[1]//div[1]//button[1]"))).click() 
                        self.driver.get_screenshot_as_file("screenshots/TestCase11_03_ConfirmDeleteTag.png")                         
            self.driver.get("http://134.209.63.241:8080/mua2/")
            self.driver.get_screenshot_as_file("screenshots/TestCase11_04_HomePage.png")                                          
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase12_login(self):
        try:
            print("***** Test Case 12 - Login *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            self.driver.get_screenshot_as_file("screenshots/TestCase12_01_GoTagsPage.png") 
            self.driver.find_element_by_xpath("//input[@ng-model='usuario.name']").send_keys("admin")
            self.driver.find_element_by_xpath("//input[@ng-model='usuario.password']").send_keys("admin")
            self.driver.get_screenshot_as_file("screenshots/TestCase12_02_TypeLogin.png") 
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//button[@class='btn btn-primary']"))).click()
            time.sleep(5)     
            self.driver.get_screenshot_as_file("screenshots/TestCase12_03_CheckLogin.png") 
        except NoSuchElementException as e:
            print (e)
            return False
        return True

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Repository/automatedtest/Tests",report_title="MUA Test",descriptions="MUA Test Cases Results", verbosity=2))