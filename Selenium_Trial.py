from selenium import webdriver
from selenium.webdriver.common.by import By

def Find_Wealthiest_Merchant():
    # Items were not pulled directly into a dictionary because pycharm warned that the input was too long
    # If I had more time I could have cleaned up this pulling process
    riddle_3_name_1 = browser.find_element(By.XPATH, "//h2[contains(text(), 'The Two Merchants')]/.. /div[3]/span").text
    riddle_3_wealth_1 = int(browser.find_element(By.XPATH, "//h2[contains(text(), 'The Two Merchants')]/.. /div[3]/p").text)
    riddle_3_name_2 = browser.find_element(By.XPATH, "//h2[contains(text(), 'The Two Merchants')]/.. /div[4]/span").text
    riddle_3_wealth_2 = int(browser.find_element(By.XPATH, "//h2[contains(text(), 'The Two Merchants')]/.. /div[4]/p").text)

    # Build dictionary based on the information pulled from the target website
    wealth_tracker = {riddle_3_name_1:riddle_3_wealth_1, riddle_3_name_2:riddle_3_wealth_2}
    # Get the wealthiest person from the key, based on the value pulled from the target website
    wealthiest_merchant = max(wealth_tracker, key=wealth_tracker.get)
    return wealthiest_merchant


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

# Get the wealthiest merchant for question 3
riddle_3_result = Find_Wealthiest_Merchant()

# Input the final answer via CSS
browser.find_element(By.CSS_SELECTOR, "input[id='r3Input']").send_keys(riddle_3_result)

# Click button to submit first answer via CSS
browser.find_element(By.CSS_SELECTOR, "button[id='r3Butn']").click()

# Click Check Answers Button
browser.find_element(By.CSS_SELECTOR, "button[id='checkButn']").click()

# Trial Completed
try:
    trial_result = browser.find_element(By.XPATH, "//div[@id='trialCompleteBanner']/h4").text
except:
    print("You did not pass the trial")
else:
    print("You passed the trial")
