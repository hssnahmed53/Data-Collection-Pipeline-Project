from utils.scraper import Scraper
import time

if __name__ == '__main__':
    bot = Scraper()
    bot.accept_cookies()
    time.sleep(5)
    bot.best_sellers()
    time.sleep(5)