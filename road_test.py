from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def sign_in(driver, last_name, license_number, keyword):
    input_last_name = driver.find_element_by_id("mat-input-0").send_keys(last_name)
    input_license_number = driver.find_element_by_id("mat-input-1").send_keys(license_number)
    input_keyword = driver.find_element_by_id("mat-input-2").send_keys(keyword)

    
    check_box = driver.find_element_by_id("mat-checkbox-1-input")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(check_box).click(check_box).perform()

    sign_in = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]")
    #print(sign_in)
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(sign_in).click(sign_in).perform()

    return

def search_location (driver):
    location = driver.find_element_by_id('mat-input-3')
    driver.implicitly_wait(10)
    location.send_keys('Burnaby')
    ActionChains(driver).move_to_element(location).click(location).perform()
    location.send_keys(' ')

    drop_down = driver.find_element_by_xpath("//div[@id='mat-autocomplete-0']//span[contains(text(), 'Burnaby, BC')]").click()
    search = driver.find_element_by_xpath("//button[@class ='mat-raised-button mat-button-base search-button mat-accent']").click()
    return

if __name__ == "__main__":

    
    last_name = input("Enter your last name: ")
    license_number = input("Enter your license number: ")
    keyword = input("Enter your keyword: ")

    driver = webdriver.Chrome("chromedriver_win32\chromedriver")
    driver.get("https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver")

    sign_in(driver, last_name, license_number, keyword)
    search_location(driver)

    select_location = driver.find_element_by_xpath("//div[contains(text(), 'Burnaby driver licensing')]").click()

    # close the driver
    driver.close()