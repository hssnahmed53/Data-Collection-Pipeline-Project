from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self, url:str = 'https://www.waterstones.com/'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def accept_cookies (self, xpath: str = '//button[@id="onetrust-accept-btn-handler"]'):
        
            '''
            Finds and clicks the "Accept" button for the cookies

            Parameters
            ----------
            xpath: str
                The Xpath of the accept cookies button
            '''
            accept_cookies = self.driver.find_element(By.XPATH, xpath)
            accept_cookies.click()
    
    def best_sellers (self, xpath: str = '//*[@id="pagesmain"]/div[3]/header[4]/a'):
        
            '''
            Finds and clicks the "See more" button for the best sellers

            Parameters
            ----------
            xpath: str
                The Xpath of the see more button
            '''
            best_sellers = self.driver.find_element(By.XPATH, xpath)
            best_sellers.click()

    def scroll(self):
        '''
        Scrolls the page
        '''
        """This function locates the product pages and then collects the URL of each page."""
        self.driver.execute_script("window.scrollBy(0,500)")

    def book_preview(self, xpath: str = '//*[@id="p_11568365"]/div/div[1]/div/a/img'): 