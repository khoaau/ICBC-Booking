from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def find_date_by_location(location, driver):
    # print(location)
    select_location = driver.find_element_by_id('step2')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(select_location).click(select_location).perform()

    string = "//*[contains(text(), '"+ location +"' )]"
    button = driver.find_element_by_xpath(string)
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()


    select_date_time = driver.find_element_by_id('step3')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(select_date_time).click(select_date_time).perform()



    # next_month = driver.find_element_by_xpath("//*[contains(text(), 'chevron_right')]")
    # driver.implicitly_wait(10)
    # ActionChains(driver).move_to_element(next_month).click(next_month).perform()

    # driver.implicitly_wait(10)
    # ActionChains(driver).move_to_element(next_month).click(next_month).perform()

    list_dates = []
    find_date = True
    month = ''
    while find_date:
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        list_dates.clear()
        for m in soup.findAll('div', attrs={'style': 'color: rgb(0, 157, 224); caret-color: rgb(0, 157, 224);'}):
            # print(m.text)
            month = m.text

        for a in soup.findAll('button',attrs={'class':'v-btn v-btn--flat v-btn--floating theme--light'}):
            # print(a.text)
            if a.text:
                list_dates.append(a.text)
        
        if len(list_dates) > 0:
            find_date = False
        else:
            next_month = driver.find_element_by_xpath("//*[contains(text(), 'chevron_right')]")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(next_month).click(next_month).perform()
    
    return month, list_dates[0]

def choose_earliest_date (locations):
    dic = {'January': 1, 'Febuary': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    earliest_month = 13
    earliest_date = 32
    location = ''
    for i in locations:
        if dic[i['month']] < earliest_month:
            earliest_month = dic[i['month']]
            location = i['location']
        elif dic[i['month']] == earliest_month:
            if int(i['date']) < earliest_date:
                earliest_date = int(i['date'])

    return location

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver_win32\chromedriver")
    driver.get("https://onlinebusiness.icbc.com/qmaticwebbooking/#/")

    test_type = driver.find_element_by_id("da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(test_type).click(test_type).perform()

    locations = ['Burnaby','Vancouver Burrard Station – Royal Centre','Metrotown', 'East Van', 'Point Grey']
    object_location = []
    for i in locations:
        month, earliest_date = find_date_by_location(i, driver)
        new_obj = {'location': i, 'month': month[:-5], 'date': earliest_date}
        object_location.append(new_obj)
    print(object_location)

    best_location = choose_earliest_date(object_location)
    print(best_location)

    close the driver
    driver.close()