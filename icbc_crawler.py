from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 10)


def Login():
    browser.get('https://onlinebusiness.icbc.com/webdeas-ui/home')
    nextButton = browser.find_element_by_css_selector('body > app-root > app-home > mat-card > div.content > div.form-control > button')
    nextButton.click()

    lastname = browser.find_element_by_id("mat-input-0")
    licenseNum = browser.find_element_by_id("mat-input-1")
    keyword = browser.find_element_by_id("mat-input-2")

    lastname.send_keys("Jing")
    licenseNum.send_keys("1951523")
    keyword.send_keys("Zhang")

    agree = browser.find_element_by_css_selector('#mat-checkbox-1 > label > span.mat-checkbox-inner-container')
    agree.click()

    signIn = browser.find_element_by_css_selector('body > app-root > app-login > mat-card > mat-card-content > form > div.form-control.action-buttons.mat-dialog-actions > button.mat-raised-button.mat-button-base.mat-accent > span')
    signIn.click()

    Reschedule()

    location = wait.until(EC.visibility_of_element_located((By.ID, 'mat-input-3')))
    text = "4233 Cartier"
    for character in text:
        location.send_keys(character)
        time.sleep(0.2)

    location.send_keys(Keys.ENTER)

    search = browser.find_element_by_css_selector('#search-dialog > app-search-modal > div > div > form > div.search-action.mat-dialog-actions.ng-star-inserted > button')
    search.click()

def Reschedule():
    WebDriverWait(browser, 3)

    rescheduleButton = browser.find_element_by_css_selector('body > app-root > app-driver > div > mat-card > div.mat-typography > div.appointments-cards-container > app-appointments > div > div.appointment-content.ng-star-inserted > div > div.button-group.mat-dialog-actions > button:nth-child(1) > span')
    rescheduleButton.click()

    WebDriverWait(browser, 3)

    confirmRescheduleButton = browser.find_element_by_css_selector('#mat-dialog-0 > app-cancel > div > div > div.form-control.otp-action-buttons.mat-dialog-actions > button.mat-raised-button.mat-button-base.mat-accent.ng-star-inserted')
    confirmRescheduleButton.click()

    WebDriverWait(browser, 3)

def BookAppointment():
    firstAvailableTime = browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-eligible-tests/div/div[2]/mat-button-toggle-group/div/div/following-sibling::mat-button-toggle')
    firstAvailableTime.click()
    reviewButton = browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-eligible-tests/div/div[3]/button[2]')
    reviewButton.click()
    time.sleep(0.2)
    nextButton = browser.find_element_by_xpath('//*[@id="mat-dialog-1"]/app-booking-review/div/div[2]/div[2]/button[2]/span')
    nextButton.click()
    time.sleep(0.2)
    smsOption = browser.find_element_by_xpath('//*[@id="mat-dialog-2"]/app-onetime-password/div/div[1]/form/div[2]/div[1]/input')
    smsOption.click()
    sendButton = browser.find_element_by_xpath('//*[@id="mat-dialog-2"]/app-onetime-password/div/div[2]/button[2]')
    sendButton.click()

def Refresh(wait_time =32):
    try:
        pgLocationSelected = browser.find_element_by_xpath("//*[contains(text(), '4126 Macdonald St')]")
#        lougheedLocationSelected = browser.find_element_by_xpath("//*[contains(text(), '3880 Lougheed Hwy')]")
        while(True):
            pgLocationSelected.click()
            time.sleep(wait_time)
            firstAvailableDate = browser.find_elements_by_class_name('date-title')[0]
            earliestMonth = firstAvailableDate.text.split(",")[1].strip().split()[0].strip()
            if earliestMonth == "April":
                break
        print("FOUND APPOINTMENT!!!!!!!")
        BookAppointment()
    except:
        # if we run into an error then redo login
        Login()
        Refresh()

Login()
Refresh()
