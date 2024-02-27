from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
text = "hello"
# Ask the user to input the PIN
pin = input("Please enter a 14-digit PIN: ")

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Firefox()

# Open the website
driver.get('https://www.cookcountypropertyinfo.com/')
wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1 
driver.maximize_window()


try:
    # Find the input field and input the PIN
    driver.implicitly_wait(10)
    search_box = driver.find_element(By.ID,'pinBox1')
    print("test")
    search_box.send_keys(pin)
    search_box.submit()
    

    # Submit the form
    submit_button = driver.find_element(By.ID, 'ContentPlaceHolder1_PINAddressSearch_btnSearch')
    submit_button.click()

    # Wait for the page to load (you may need to adjust the waiting time)
    driver.implicitly_wait(5)

    # Get the resulting page HTML
    page_source = driver.page_source

    # Save the page as HTML file
    with open('downloaded_page.html', 'w', encoding='utf-8') as file:
        file.write(page_source)
       
finally:
    driver.switch_to.new_window('tab')
    
    driver.get('https://www.cookcountytreasurer.com/setsearchparameters.aspx')
try:
    driver.implicitly_wait(10)
    search_box2 = driver.find_element(By.ID,'ContentPlaceHolder1_ASPxPanel1_SearchByPIN1_txtPIN1')
    search_box2.send_keys(pin)
    driver.implicitly_wait(5)
    search_box2.submit()
    submit2 = driver.find_element(By.NAME,'ctl00$ContentPlaceHolder1$ASPxPanel1$SearchByPIN1$cmdContinue')
    submit2.click()
    driver.implicitly_wait(5)
    
    
    
finally:
    driver.switch_to.new_window('tab')
    driver.get('https://crs.cookcountyclerkil.gov/Search')
    driver.implicitly_wait(5)
    search_box3 = driver.find_element(By.ID, 'inputField')
    search_box3.send_keys(pin)
    
    search_box3.submit()
    button3 = driver.find_element(By.ID, 'btnAddressSearch')
    button3.click()
    driver.implicitly_wait(5)
    
    
    
    
    
try:
   
    driver.implicitly_wait(15)

finally:
    # Close the browser
    driver.implicitly_wait(15)