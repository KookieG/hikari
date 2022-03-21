import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

names = open('names.txt', 'r').read().split('\n')
available = open('available.txt', 'w')
taken = open('taken.txt', 'w')

def check():
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    for i in names:
        driver.get(f"https://anilist.co/user/{i}")
        try:
            WebDriverWait(driver, 1.5).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[1]/h1"))
            )
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[1]/h1")
            print(f"{i} is taken")
            taken.write(f"{i}\n")
        except:
            print(f"{i} is available")
            available.write(f"{i}\n")
    driver.close()
    input("done checking, press enter to close.")
    
if __name__ == '__main__':
    check()