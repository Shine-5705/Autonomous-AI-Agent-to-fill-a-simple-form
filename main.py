from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Selenium WebDriver (Make sure to specify the path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the form URL
driver.get("https://form.jotform.com/241617189501153")

# Give the page some time to load
time.sleep(3)

# Fill in the Full Name fields
first_name_field = driver.find_element(By.XPATH, '//*[@id="first_3"]')
first_name_field.send_keys("Shine")
middle_name_field = driver.find_element(By.XPATH, '//*[@id="middle_3"]')
middle_name_field.send_keys(" ")
last_name_field = driver.find_element(By.XPATH, '//*[@id="last_3"]')
last_name_field.send_keys("Gupta")

# Fill in the Current Address fields
street_address_field = driver.find_element(By.XPATH, '//*[@id="input_5_addr_line1"]')
street_address_field.send_keys("Sanjay Colony phase 2")
street_address_line2_field = driver.find_element(By.XPATH, '//*[@id="input_5_addr_line2"]')
street_address_line2_field.send_keys("near KIET Group of Institutions")
city_field = driver.find_element(By.XPATH, '//*[@id="input_5_city"]')
city_field.send_keys("Ghaziabad")
state_field = driver.find_element(By.XPATH, '//*[@id="input_5_state"]')
state_field.send_keys("Uttar Pradesh")
postal_code_field = driver.find_element(By.XPATH, '//*[@id="input_5_postal"]')
postal_code_field.send_keys("201206")

# Fill in the Email field
email_field = driver.find_element(By.XPATH, '//*[@id="input_4"]')
email_field.send_keys("guptashine5002@gmail.com")

# Fill in the Phone Number field
phone_field = driver.find_element(By.XPATH, '//*[@id="input_6_phone"]')
phone_field.send_keys("8433135192")

# Fill in the LinkedIn field
linkedin_field = driver.find_element(By.XPATH, '//*[@id="input_7"]')
linkedin_field.send_keys("https://www.linkedin.com/in/shine-gupta-62b22b264/")

# Write something interesting about AI Agents/LLMs
ai_agents_field = driver.find_element(By.XPATH, '//*[@id="input_10"]')
ai_agents_field.send_keys("AI agents and large language models (LLMs) are transforming the way we interact with technology, enabling more natural and efficient communication between humans and machines.")

# Write something interesting about Web Automation
web_automation_field = driver.find_element(By.XPATH, '//*[@id="input_11"]')
web_automation_field.send_keys("Web automation streamlines repetitive tasks, reduces human error, and improves productivity by leveraging tools like Selenium to interact with web elements programmatically.")

# Reverse a LinkedList (dummy text)
reverse_linkedlist_field = driver.find_element(By.XPATH, '//*[@id="input_12"]')
reverse_linkedlist_field.send_keys("To reverse a LinkedList, you can iterate through the list, changing the next pointers of each node to point to the previous node.")

# Upload a resume
resume_upload_field = driver.find_element(By.XPATH, '//*[@id="input_8"]')
resume_upload_field.send_keys('Autonomous-AI-Agent-to-fill-a-simple-form/Shine resume_.pdf')  

# Fill in the Cover Letter field
cover_letter_field = driver.find_element(By.XPATH, '//*[@id="input_9"]')
cover_letter_field.send_keys("This is a dummy cover letter for testing purposes.")

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="input_2"]')
submit_button.click()

# Wait for a while to see the result
time.sleep(5)

# Close the browser
driver.quit()
