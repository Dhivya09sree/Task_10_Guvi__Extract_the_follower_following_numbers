from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class guvi_Extract_the_follower_following_numbers:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15

    # Initialize the ChromeDriver
    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    # Open a website
    def open_website(self, url):
        self.driver.get(url)

   # Maximize the browser window
    def maximize_window(self):
        self.driver.maximize_window()

    #Extract the total number of follower
    def Extract_the_total_number_of_follower(self):
        follower = self.driver.find_element(By.XPATH,"(//button[@type='button'])[3]")
        follower_text = follower.text
        print ("Total number of follower on Guvi Page :",follower_text)

    # Extract the total number of following
    def Extract_the_total_number_of_following(self):
        following = self.driver.find_element(By.XPATH, "(//button[@type='button'])[4]")
        following_text = following.text
        print("Total number of following on Guvi Page :", following_text)


    def close(self):
        self.driver.close()

#create a object
guvi = guvi_Extract_the_follower_following_numbers()

#Initialize the browser
guvi.initialize_driver()
time.sleep(2)

#open the website
guvi.open_website("https://www.instagram.com/guviofficial/")
time.sleep(2)

# Maximize the window
guvi.maximize_window()
time.sleep(2)

#Extract the total number of follower On Guvi page
guvi.Extract_the_total_number_of_follower()
time.sleep(3)

#Extract the total number of following On Guvi page
guvi.Extract_the_total_number_of_following()
time.sleep(3)

# Close the browser
guvi.close()


