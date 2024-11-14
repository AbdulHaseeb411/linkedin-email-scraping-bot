from linkedin_scaper import setup_driver, login_linkedin, scrape_email
from csv_utils import read_profiles_from_csv, save_to_csv

def main(input_filename, output_filename, username, password):
    profile_urls = read_profiles_from_csv(input_filename)
    driver = setup_driver()
    login_linkedin(driver, username, password)
    
    for profile_url in profile_urls:
        email = scrape_email(driver, profile_url)
        if email:
            save_to_csv([profile_url, email], output_filename)
            print(f"Email for {profile_url} saved: {email}")
        else:
            print(f"No email found for {profile_url}")
    
    driver.quit()


input_filename = "profile_urls.csv"  
output_filename = "linkedin_emails.csv"  


username = "your_email@example.com"
password = "your_password"

main(input_filename, output_filename, username, password)
