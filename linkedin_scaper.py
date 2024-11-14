import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_driver():
    """Set up and return a Selenium WebDriver instance."""
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    return driver

def login_linkedin(driver, username, password):
    """Log in to LinkedIn using provided credentials."""
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)  

def scrape_email(driver, profile_url):
    """Navigate to a LinkedIn profile URL and scrape the email if available."""
    driver.get(profile_url)
    time.sleep(2) 
    
    try:
       
        driver.find_element(By.XPATH, "//a[@data-control-name='contact_see_more']").click()
        time.sleep(1)
        

        email_element = driver.find_element(By.XPATH, "//section[@class='pv-contact-info__contact-type ci-email']//a")
        email = email_element.text
        return email
    
    except Exception as e:
        print(f"Could not find email for {profile_url}: {e}")
        return None
