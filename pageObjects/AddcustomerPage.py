import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemsAdmistrators_xpath = "//li[normalize-space()='Administrators']"
    lstitemsRegistered_xpath = "//li[@id='06a87908-f59f-4893-85f1-460b3d1074a6']"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
    def clickonCustomermenuitem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
    def clickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)
    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemsRegistered_xpath)
        elif role == 'Administrators':
            self.listitem =self.driver.find_element(By.XPATH,self.lstitemsAdmistrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath).click()
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemsRegistered_xpath)
        elif role == 'Vendors':
            self.listitem =self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem =self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)   # works as a click option
    def setManagerOfVendors(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)
    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)
    def setCompanyName(self,company):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(company)
    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()


