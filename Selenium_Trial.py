from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# Input first answer via CSS
browser.find_element(By.CSS_SELECTOR, "input[id='r1Input']").send_keys("rock")

# Click button to submit first answer via CSS
browser.find_element(By.CSS_SELECTOR, "button[id='r1Btn']").click()

# Store password from output of first to use as the answer in the next question via XPATH
riddle_1_result = browser.find_element(By.XPATH, "//div[@id='passwordBanner']/h4")

# Input second answer via CSS, using output from riddle_1
browser.find_element(By.CSS_SELECTOR, "input[id='r2Input']").send_keys(riddle_1_result.text)

# Click button to submit second answer via CSS
browser.find_element(By.CSS_SELECTOR, "button[id='r2Butn']").click()


#input_2_path = "input[id='r2Input']"
#input_2_element = browser.find_element(By.CSS_SELECTOR, input_2_path)
