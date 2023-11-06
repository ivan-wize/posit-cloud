from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def log_in():
    # Open the login page
    driver.get("https://posit.cloud")

    # Click the login button
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Log In']]")))
    login_link.click()

    # Wait for the email input to be visible and then input the email
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    email_input.send_keys("ivan.wize+posit.test@gmail.com")

    # Wait for the continue button to be clickable and then click it
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Continue']]")))
    continue_button.click()

    # Wait for the password input to be visible and then input the password
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys("posittest123")

    # Wait for the login button to be clickable and then click it
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Log In']]")))
    login_button.click()

    time.sleep(1)

def create_new_space():
    # After login, wait for the "New Space" button to appear and click it
    new_space_button = "//span[text()='New Space']"
    new_space = wait.until(EC.element_to_be_clickable((By.XPATH, new_space_button)))
    new_space.click()

    time.sleep(1)

    # Create the new space
    new_space_name_field = driver.find_element(By.ID, "name")
    new_space_name_field.click()
    new_space_name_field.send_keys("Test Space")

    # Wait for the "Create" button to be clickable
    create_button = "//button[.//span[text()='Create']]"
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH, create_button)))
    create_button.click()

    time.sleep(1)

def delete_space():
    # Select the newly created space
    test_space = (By.XPATH, "//div[@class='spaceNameWithOwner' and contains(text(), 'Test Space')]")
    test_space = wait.until(EC.presence_of_element_located(test_space))
    test_space.click()

    time.sleep(1)

    # Perform actions on the test space
    button_locator = "//button[@aria-label='Test Space: More Actions']"
    button = wait.until(EC.element_to_be_clickable((By.XPATH, button_locator)))
    button.click()

    time.sleep(1)

    # Initiate deletion of the test space
    delete_button_locator = By.ID, "headerDeleteSpaceButton"
    delete_button = wait.until(EC.visibility_of_element_located(delete_button_locator))
    delete_button.click()

    time.sleep(1)

    # Confirm deletion of the test space
    delete_input_locator = By.ID, "deleteSpaceTest"
    input_element = wait.until(EC.visibility_of_element_located(delete_input_locator))
    input_element.click()
    input_element.send_keys("Delete Test Space")

    time.sleep(1)

    # Submit deletion
    submit_button_locator = By.ID, "deleteSpaceSubmit"
    submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
    submit_button.click()

    time.sleep(3)

# Perform the actions
log_in()
create_new_space()
delete_space()

# Close the driver
driver.quit()
