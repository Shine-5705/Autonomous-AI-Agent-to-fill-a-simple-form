import openai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate text using OpenAI GPT-3.5-turbo
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the JotForm page
driver.get("https://form.jotform.com/241617189501153")

# Wait for the page to load
time.sleep(10)

# Fill in the Name fields
driver.find_element(By.XPATH, '//*[@id="first_11"]').send_keys("Shine")
driver.find_element(By.XPATH, '//*[@id="middle_11"]').send_keys(" ")
driver.find_element(By.XPATH, '//*[@id="last_11"]').send_keys("Gupta")

# Fill in the Current Address fields
driver.find_element(By.XPATH, '//*[@id="input_16_addr_line1"]').send_keys("Sanjay Colony phase 2")
driver.find_element(By.XPATH, '//*[@id="input_16_addr_line2"]').send_keys("near KIET Group of Institutions")
driver.find_element(By.XPATH, '//*[@id="input_16_city"]').send_keys("Ghaziabad")
driver.find_element(By.XPATH, '//*[@id="input_16_state"]').send_keys("Uttar Pradesh")
driver.find_element(By.XPATH, '//*[@id="input_16_postal"]').send_keys("201206")

# Fill in the Email field
driver.find_element(By.XPATH, '//*[@id="input_12"]').send_keys("guptashine5002@gmail.com")

# Fill in the Phone Number field
driver.find_element(By.XPATH, '//*[@id="input_13_full"]').send_keys("+91 8433135192")

# Fill in the LinkedIn field
driver.find_element(By.XPATH, '//*[@id="input_19"]').send_keys("https://www.linkedin.com/in/shine-gupta-62b22b264/")

# Generate and fill in the AI Agents/LLMs field
ai_agents_text = generate_text("Write something interesting about AI Agents/LLMs.")
driver.find_element(By.XPATH, '//*[@id="input_24"]').send_keys(ai_agents_text)

# Generate and fill in the Web Automation field
web_automation_text = generate_text("Write something interesting about Web Automation.")
driver.find_element(By.XPATH, '//*[@id="input_25"]').send_keys(web_automation_text)

# Fill in the Reverse a LinkedList (dummy text)
driver.find_element(By.XPATH, '//*[@id="input_23"]').send_keys("To reverse a LinkedList, you can iterate through the list, changing the next pointers of each node to point to the previous node.")

# Upload a resume
resume_path = os.path.join(os.getcwd(), 'Shine resume_.pdf')
driver.find_element(By.XPATH, '//*[@id="input_17"]').send_keys(resume_path)

# Generate and fill in the Cover Letter field
cover_letter_text = generate_text("Write a cover letter for a job application.")
driver.find_element(By.XPATH, '//*[@id="input_22"]').send_keys(cover_letter_text)

# Submit the form
driver.find_element(By.XPATH, '//*[@id="input_9"]').click()

# Wait for a while to see the result
time.sleep(5)

# Close the browser
driver.quit()
