import unittest, time, HtmlTestRunner, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored

class MuaTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Python\\Testing\\chromedriver_win32\\chromedriver.exe")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.driver.get("http://157.230.152.226:8080/mua/#!/")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver = None
    
    def test_case_01(self):
        try:
            print("***** Test Case 01 - Create new Category *****")
            self.driver.get("http://157.230.152.226:8080/mua/#!/ejemplos")
            self.driver.find_element_by_xpath("//i[@ng-click='setGuardar()']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveCategory.nombre']").send_keys("Test01")
            self.driver.find_element_by_xpath("//input[@ng-model='formSaveCategory.nombre']").send_keys(u'\ue007')
            self.driver.get_screenshot_as_file("screenshots/TestCase01_01_NewCategory.png")
            self.driver.get("http://157.230.152.226:8080/mua/#!")
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
            self.driver.get("http://157.230.152.226:8080/mua/#!/ejemplos")
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
            self.driver.get("http://157.230.152.226:8080/mua/#!/nuevoPost")
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
            self.driver.get("http://157.230.152.226:8080/mua/#!/nuevoPost")
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
            self.driver.get("http://157.230.152.226:8080/mua/#!/nuevoPost")
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
            self.driver.find_element_by_id("titulo").send_keys("Lorem Ipsum Generator")
            self.driver.find_element_by_id("descripcion").clear()
            self.driver.find_element_by_id("descripcion").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")            
            self.driver.get_screenshot_as_file("screenshots/TestCase12_02_EditPost.png")            
            self.driver.find_element_by_xpath("//select[@id='categoria' and @ng-model='currentCategory']//option[4]").click()
            self.driver.find_element_by_xpath("//div[@class='btn btn-primary' and @ng-click='showAdvanced()']//i[1]").click()
            self.driver.find_element_by_name("file").send_keys("C:\\Repository\\automatedtest\\screenshots\\jpg.jpg")
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

    '''def test_case_17(self):
        try:
            #By the moment this feature is unable
            print("***** Test Case 17 - Delete Posts *****")
            #self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[5]").click()
            self.driver.find_element_by_xpath("//select[@ng-model='busqueda.categoria']//option[@value='Test01']").click()
            self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[2]//div[3]//a[2]").click()
            #self.driver.find_element_by_xpath("//a[@href='#!/editPost/160']").click() 
            time.sleep(5)
            self.driver.find_element_by_xpath("//i[@class='fas fa-trash fa-3x']").click()
            self.driver.get_screenshot_as_file("screenshots/TestCase17_01_DeletePost.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True'''

    def test_case_18(self):
        try:
            print("***** Test Case 18 - Edit Categories *****")
            self.driver.get("http://157.230.152.226:8080/mua/#!/ejemplos")
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

    '''def test_case_19(self):
        try:
            #By the moment this feature is blocked, we aren't not able to delete assigned Post
            print("***** Test Case 19 - Delete Categories *****")
            self.driver.get("http://157.230.152.226:8080/mua/#!/ejemplos")
            self.driver.get_screenshot_as_file("screenshots/TestCase19_01_AccessCategories.png") 
            time.sleep(5) 
            rows = len(self.driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))
            for row in range(rows+1):
                if (row>1):
                       if (self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Test01'):         
                            self.driver.find_element_by_xpath("//table[@class='table table-striped']//tbody//tr[%d]//td[3]//i[2]" % (row)).click()
                            time.sleep(5)
                            self.driver.get_screenshot_as_file("screenshots/TestCase19_02_DeleteCategory.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True'''
    
    def test_case_20(self):
        try:
            print("***** Test Case 20 - Create New Tags *****")
            self.driver.get("http://157.230.152.226:8080/mua/#!/tags")
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
            self.driver.get("http://157.230.152.226:8080/mua/#!/tags")
            time.sleep(5)
            #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/TestCase21_01_TagsRows.png") 
            rows = len(self.driver.find_elements_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr"))
            for row in range(rows+1):
                if (row>1):                
                    if (self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[2]" % (row)).get_attribute("innerHTML") == 'Test01 Updated'):   
                        self.driver.find_element_by_xpath("//div[@class='container']//div[1]//div[1]//div[2]//table//tbody//tr[%d]//td[4]//i[1]" % (row)).click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_02_AccessEditTagsPage.png") 
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.nombre']").clear()
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.nombre']").send_keys("Test01 2018")
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.descripcion']").clear()
                        self.driver.find_element_by_xpath("//input[@ng-model='formTags.descripcion']").send_keys("Test01 Tag")
                        self.driver.find_element_by_xpath("//div[@ng-show='editar']//form//button[1]").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_03_TagsUpdated.png")
                        self.driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()
                        self.driver.get_screenshot_as_file("screenshots/TestCase21_04_TagsExit.png")
        except NoSuchElementException as e:
            print (e)
            return False
        return True

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Repository/automatedtest/Tests",report_title="MUA Test",descriptions="MUA Test Cases Results", verbosity=2))