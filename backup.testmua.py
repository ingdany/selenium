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
        self.driver.get("http://134.209.63.241:8080/mua/#!/")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver = None
    
    def test_case_01(self):
        try:
            print("***** Test Case 01 - Create new Category *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/ejemplos")
            self.driver.find_element_by_xpath("//i[@ng-click='setGuardar()']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveCategory.nombre']").send_keys("Test01")
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveCategory.nombre']").send_keys(u'\ue007')
            self.driver.get_screenshot_as_file("screenshots/TestCase01_01_NewCategory.png")
            self.driver.get("http://134.209.63.241:8080/mua/#!")
            self.driver.get_screenshot_as_file("screenshots/TestCase01_02_ReturnHome.png")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value=Test01']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase01_03_ViewCategories.png")
            time.sleep(5)
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_02(self):
        print("***** Test Case 02 - View Category in Main Page *****")
        self.driver.get_screenshot_as_file("screenshots/TestCase02_01_VerifyDefaultCategory.png")
        self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
        self.driver.get_screenshot_as_file("screenshots/TestCase02_02_FilterByCategory.png")
    
    def test_case_03(self):
        try:
            print("***** Test Case 03 - Select non-valid Category in Main Page *****")
            self.driver.get_screenshot_as_file("screenshots/TestCase03_01_AccessMainPage.png") 
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value=' ']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase03_02_NonCategory.png") 
            self.driver.quit()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_04(self):
        try:
            print("***** Test Case 04 - View Categories  *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/ejemplos")
            self.driver.get_screenshot_as_file("screenshots/TestCase04_01_AccessCategoryPage.png")
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):
                    if (self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[2]" %(row)).get_attribute("innerHTML") == 'Test01'):
                        self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[3]//i[1]" % (row)).click()            
                        self.driver.get_screenshot_as_file("screenshots/TestCase04_02_ViewCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_05(self):
        try:
            print("***** Test Case 05 - Create new Post attaching PNG image *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/nuevoPost")
            self.driver.find_element_by_xpath("//input[@ng-model='nuevoPost.titulo']").send_keys("Automatic Post 1")
            self.driver.find_element_by_xpath("//select[@ng-model='currentCategory']//option[@label='Test01']").click()
            self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()      
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\png.png")
            self.driver.get_screenshot_as_file("screenshots/TestCase05_01_BrowsePNGImage.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase05_02_CheckPost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_06(self):
        try:
            print("***** Test Case 06 - Create new Post attaching BMP image *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/nuevoPost")
            self.driver.find_element_by_xpath("//input[@ng-model='nuevoPost.titulo']").send_keys("Automatic Post 2")
            self.driver.find_element_by_xpath("//select[@ng-model='currentCategory']//option[@label='Test01']").click()
            self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()        
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\bmp.bmp")
            self.driver.get_screenshot_as_file("screenshots/TestCase06_01_BrowseBMPImage.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase06_02_CheckPost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_07(self):
        try:
            print("***** Test Case 07 - Create new Post attaching JPEG image *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/nuevoPost")
            self.driver.find_element_by_xpath("//input[@ng-model='nuevoPost.titulo']").send_keys("Automatic Post 3")
            self.driver.find_element_by_xpath("//select[@ng-model='currentCategory']//option[@label='Test01'']").click()
            self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()         
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\jpg.jpg")
            self.driver.get_screenshot_as_file("screenshots/TestCase07_01_BrowseJPGImage.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase07_02_ConfigurePost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_08(self):
        try:
            print("***** Test Case 08 - Search added post in Home Page *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase08_01_FilterByCategory.png")
            #Search added post
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[2]//div[@class='card ng-scope']"))
            for row in range(rows+3):
                if (row>2):
                    self.driver.get_screenshot_as_file("screenshots/TestCase08_02_CheckFilterByCategory.png")
                    self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[%d]/h1[1]" % (row)).get_attribute("innerHTML") == 'Automatic Post...'):
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[%d]//a[1]//button[1]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase08_03_ShowPost%d.png" % (row))
                        self.driver.find_element_by_xpath("//a[@href='#!/']").click()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
     
    def test_case_09(self):
        try:
            print("***** Test Case 09 - Select a non-valid Post *****")
            self.driver.get_screenshot_as_file("screenshots/TestCase09_01_CheckPage.png")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase09_02_AnotherCategory.png") 
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[1]//button[1]").click()            
            self.driver.get_screenshot_as_file("screenshots/TestCase09_03_NotExistPost.png")
        except NoSuchElementException as e:
            print(e)
            return False
        return True 

    def test_case_10(self):
        try:
            print("***** Test Case 10 - Search post by a valid date *****") 
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker']").clear()
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker2']").clear()
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker']").send_keys("2019-01-01")
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker2']").send_keys("2019-01-02")
            self.driver.get_screenshot_as_file("screenshots/TestCase10_01_ValidDate.png")     
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_11(self):
        try:
            print("***** Test Case 11 - Search Post by invalid date  *****") 
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker']").clear()
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker2']").clear()
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker']").send_keys("2019-01-01")
            self.driver.find_element_by_xpath("//input[@ng-model='datePicker2']").send_keys("2018-01-02")
            self.driver.get_screenshot_as_file("screenshots/TestCase11_01_InValidDate.png")  
        except NoSuchElementException as e:
            print (e)
            return False
        return True
   
    def test_case_12(self):
        try:
            print("***** Test Case 12 - Edit Post *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase12_01_GoPost.png")
            self.driver.find_element_by_id("titulo").clear()
            self.driver.find_element_by_id("titulo").send_keys("Lorem Ipsum Generator Second Edit")
            self.driver.find_element_by_id("descripcion").clear()
            self.driver.find_element_by_id("descripcion").send_keys("Morbi volutpat sapien sollicitudin suscipit venenatis. Nulla posuere orci ac vulputate sollicitudin. Cras eu fringilla sem, scelerisque bibendum libero. Aenean at magna dolor. Nullam semper posuere neque ac scelerisque. Aenean leo lectus, lacinia sit amet purus vel, feugiat pulvinar nisl. Nulla dictum porta odio, quis molestie orci molestie vitae. Maecenas interdum dolor eget purus pharetra egestas. Aliquam sed aliquam turpis. Donec ac quam quis elit venenatis maximus. Maecenas vitae nunc id velit pulvinar mattis at non diam. Morbi porta neque sed accumsan semper.")            
            self.driver.get_screenshot_as_file("screenshots/TestCase12_02_EditPost.png")            
            self.driver.find_element_by_xpath("//select[@id='categoria' and @ng-model='currentCategory']//option[4]").click()
            self.driver.find_element_by_xpath("//div[@class='btn btn-primary' and @ng-click='showAdvanced()']//i[1]").click()
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\hqdefault.jpg")
            self.driver.get_screenshot_as_file("screenshots/TestCase12_03_OpenImage.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase12_04_SavePost.png")
            self.driver.find_element_by_id("submit").click()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_13(self):
        try:
            print("***** Test Case 13 - Add image to a Post *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase13_01_EditPost.png")
            self.driver.find_element_by_xpath("//select[@id='categoria' and @ng-model='currentCategory']//option[4]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase13_02_SelectCategory.png")
            self.driver.find_element_by_xpath("//div[@class='btn btn-primary' and @ng-click='showAdvanced()']//i[1]").click()
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\png.png")
            self.driver.get_screenshot_as_file("screenshots/TestCase13_03_OpenImage.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase13_04_SavePost.png")
            self.driver.find_element_by_id("submit").click()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_14(self):
        try:
            print("***** Test Case 14 - Drop images from Post *****")
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//div[@class='ng-scope']//div[2]//i[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase14_01_DeleteImageFromPost.png")
            self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm swal-button--danger']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase14_02_ConfirmDelete.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_15(self):
        try:
            print("***** Test Case 15 - View images in Post *****")
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase15_01_PostImages.png")
            time.sleep(5)
            self.driver.find_element_by_xpath("//div[@class='ng-scope']//div[2]//div[1]//a[1]//img[1]").click()
            time.sleep(0.5)
            self.driver.get_screenshot_as_file("screenshots/TestCase15_02_SelectImage.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_16(self):
        try:
            print("***** Test Case 16 - Change Default Image in Post *****")
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase16_01_ShowPost.png") 
            time.sleep(5)
            self.driver.find_element_by_xpath("//div[@class='ng-scope']//div[2]//i[1]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase16_02_ChangeDefault.png")
            time.sleep(5)
            self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm swal-button--danger']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase16_03_ConfirmChangeDefault.png")
            time.sleep(5)
            self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase16_04_CheckCurrentImages.png")
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    def test_case_17(self):
        try:
            #By the moment this feature is unable
            print("***** Test Case 17 - Delete Posts *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase17_01_ViewPost.png")
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[4]//a[3]//i[1]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase17_02_ConfirmDeletePost.png")
            time.sleep(5)
            self.driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[2]//div[2]//button[1]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase17_03_DeletePost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_18(self):
        try:
            print("***** Test Case 18 - Edit Categories *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/ejemplos")
            self.driver.get_screenshot_as_file("screenshots/TestCase18_01_AccessCategories.png") 
            time.sleep(5) 
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):     
                    if (self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Test01'):
                        self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[3]//i[1]" % (row)).click()
                        self.driver.find_element_by_xpath("//input[@ng-model='formCategory.nombre']").clear()
                        self.driver.find_element_by_xpath("//input[@ng-model='formCategory.nombre']").send_keys("My Test")
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//button[1]").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase18_02_EditCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True  

    def test_case_19(self):
        try:
            #By the moment this feature is blocked, we aren't not able to delete assigned Post
            print("***** Test Case 19 - Delete Categories *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/ejemplos")
            self.driver.get_screenshot_as_file("screenshots/TestCase19_01_AccessCategories.png") 
            time.sleep(5) 
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):
                       if (self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Test01'):         
                            self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[4]//i[1]" % (row)).click()
                            time.sleep(5)
                            self.driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[2]//div[2]//button[1]").click()
                            self.driver.get_screenshot_as_file("screenshots/TestCase19_02_DeleteCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_20(self):
        try:
            print("***** Test Case 20 - Create New Tags *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            self.driver.get_screenshot_as_file("screenshots/TestCase20_01_AccessTagsPage.png") 
            self.driver.find_element_by_xpath("//i[@ng-click='setGuardar()']").click()             
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveTags.nombre']").send_keys("Test01")
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveTags.descripcion']").send_keys("Testing Test01 Tag")
            self.driver.get_screenshot_as_file("screenshots/TestCase20_02_CreateTagPage.png")
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[3]//form//button[1]").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase20_03_TagAdded.png")
            self.driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[3]//div[1]//button[1]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase20_04_ExitTag.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True
 
    def test_case_21(self):
        try:
            print("***** Test Case 21 - Modify Tags *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            time.sleep(5)
            #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase21_01_TagsRows.png") 
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr"))
            for row in range(rows+1):
                if (row>1):                
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Tag Updated!'):   
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[4]//i[1]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_02_AccessEditTagsPage.png") 
                        #self.driver.find_element_by_xpath("//input[@ng-model='formTags.nombre']").clear()
                        #self.driver.find_element_by_xpath("//input[@ng-model='formTags.nombre']").send_keys("Tag Updated!")
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.descripcion']").clear()
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.descripcion']").send_keys("Tag Updated!")
                        self.driver.find_element_by_xpath("//div[@ng-show='editar']//form//button[1]").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_03_TagsUpdated.png")
                        self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_04_TagsExit.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_22(self):
        try:
            print("***** Test Case 22 - Add a new post with Tags *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/nuevoPost")
            self.driver.find_element_by_xpath("//input[@ng-model='nuevoPost.titulo']").send_keys("Tag Post 9")
            self.driver.find_element_by_xpath("//select[@ng-model='currentCategory']//option[@label='Test01']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase22_01_NewPost.png")
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Tag Updated!')]"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase22_02_SelectTag.png")
            self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()      
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\png.png")
            self.driver.get_screenshot_as_file("screenshots/TestCase22_03_BrowsePNGImage.png")            
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()            
            time.sleep(5)  
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase22_04_PostAdded.png")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") 
            self.driver.get_screenshot_as_file("screenshots/TestCase22_05_CheckPost.png")
        except NoSuchElementException as e:
            print (e)
            return False    
        return True        
            
    def test_case_23(self):
        try:
            print("***** Test Case 23 - Add a tag to an existing Post *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase23_01_ShowPost.png") 
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'tag0')]"))).click()
            self.driver.get_screenshot_as_file('screenshots/TestCase23_02_TagAddedToPost.png')
            self.driver.find_element_by_id("submit").click()
        except NoSuchElementException as e:
            print (e)
            return False
        return True        

    def test_case_24(self):
        try:
            print("***** Test Case 24 - Add duplicate tags to an existing Post *****")
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase24_01_ShowPost.png") 
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'tag0')]"))).click()
            self.driver.get_screenshot_as_file('screenshots/TestCase24_02_TagAddedToPost.png')
            self.driver.find_element_by_id("submitGuardar").click()
            self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()
            wait = WebDriverWait(self.driver, 30)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'tag0')]"))).click()
            self.driver.get_screenshot_as_file('screenshots/TestCase24_03_TagAddedToPost2.png')
            self.driver.find_element_by_id("submitGuardar").click()
            self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def test_case_25(self):
        try:
            print("***** Test Case 25 - Search by Tag *****")
            wait = WebDriverWait(self.driver, 10)
            self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Tag Updated!')]"))).click()
            self.driver.get_screenshot_as_file('screenshots/TestCase25_01_TagSearch.png')
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase25_02_TagDisplay.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_26(self):
        try:
            print("***** Test Case 26 - Delete  Tag *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/tags")
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase26_01_TagsRows.png") 
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr"))
            for row in range(rows+1):
                if (row>1):                
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'tag99'):   
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[4]//i[2]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase26_02_DeleteTag.png") 
                        self.driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[2]//div[2]//button[1]").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase26_03_ConfirmDeleteTag.png") 
                        self.driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']//div[1]//div[3]//div[1]//button[1]").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase26_04_ViewPost.png") 
                        time.sleep(5)
                        self.driver.get("http://134.209.63.241:8080/mua/saveFile#!/")
                        #self.driver.get_screenshot_as_file("screenshots/TestCase26_04_ViewPost.png") 
                        wait = WebDriverWait(self.driver, 10)
                        self.driver.find_element_by_xpath("//div[@ng-model='tag']").click()
                        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'tag99')]"))).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase26_05_ViewTagInPost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_27(self):
        try:
            print("***** Test Case 27 - Create Post with Video *****")
            self.driver.get("http://134.209.63.241:8080/mua/#!/nuevoPost")
            self.driver.find_element_by_xpath("//input[@ng-model='nuevoPost.titulo']")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//input[@ng-model='nuevoPost.titulo']"))).send_keys("Automatic Test 1")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//select[@ng-model='currentCategory']//option[@label='Test01']"))).click()
            self.driver.get_screenshot_as_file("screenshots/TestCase27_01_AddPost.png")
            self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()       
            self.driver.get_screenshot_as_file("screenshots/TestCase27_02_Button.png")  
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\jpg.jpg")
            #self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\homer.mp4")
            self.driver.get_screenshot_as_file("screenshots/TestCase27_03_BrowseVideo.png")
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Upload']").click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshots/TestCase27_04_PostVideo.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def test_case_28(self):
        try:
            print("***** Test Case 28 - Add Videos to a Existing Post *****")           
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()            
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[5]//a[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase28_01_EditPost.png")
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[3]//div[1]//div[2]").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase28_02_AddVideoButton.png")     
            '''elem = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//form[@class='ng-pristine ng-valid']")))
            elem = self.driver.find_element_by_xpath("//form[@class='ng-pristine ng-valid']//input[@type='file' and @name='file']")
            elem.send_keys("C:\\Repository\\automatedtest\\screenshots\\jpg.jpg")
            print (os.getcwd())
            elem.send_keys(os.getcwd() + "\\screenshots\\homer.mp4")'''
            self.driver.get_screenshot_as_file("screenshots/TestCase28_03_VideoUploaded.png")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//form[@class='ng-pristine ng-valid']//input[@type='file' and @name='file']"))).send_keys("C:\\Repository\\automatedtest\\screenshots\\homer.mp4") 
            #WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//form[@class='ng-pristine ng-valid']//input[@type='file' and @name='file']"))).click()
            self.driver.find_element_by_xpath("//input[@type='submit' and @value='Subir video']").click() 
            #WebDriverWait(self.driver,60).until(EC.visibility_of_element_located((By.XPATH,"//form[@class='ng-pristine ng-valid']//input[@type='file' and @name='file']"))).send_keys("C:\\Repository\\automatedtest\\screenshots\\homer.mp4") 

        except NoSuchElementException as e:
            print (e)
            return False
        return True
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Repository/automatedtest/Tests",report_title="MUA Test",descriptions="MUA Test Cases Results", verbosity=2))