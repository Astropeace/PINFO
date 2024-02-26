from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ask the user to input the PIN
pin = input("Please enter a 14-digit PIN: ")

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Firefox()

# Open the website
driver.get('https://www.cookcountypropertyinfo.com/')

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
    driver2 = webdriver.Firefox()
    driver2.get('https://www.cookcountytreasurer.com/setsearchparameters.aspx')
try:
    driver2.implicitly_wait(10)
    search_box2 = driver2.find_element(By.ID,'ContentPlaceHolder1_ASPxPanel1_SearchByPIN1_txtPIN1')
    search_box2.send_keys(pin)
    search_box2.submit()
    button2 = driver2.find_element(By.ID, 'ContentPlaceHolder1_ASPxPanel1_SearchByPIN1_cmdContinue')
    button2.click()
    button2.send_keys(Keys.ENTER)
    driver2.implicitly_wait(5)
   

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()