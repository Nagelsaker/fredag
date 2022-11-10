from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import yaml
import time

T = 1
V = 0.1

def loadLogin():
    with open("login.yaml", "r") as stream:
        try:
            dict = yaml.safe_load(stream)
            uname = dict['uname']
            pword = dict['pword']
            return uname, pword
        except yaml.YAMLError as exc:
            print(exc)
            exit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.spotify.com")

    uname, pword = loadLogin()

    # login
    elem = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[6]/button[2]')
    elem.click()
    time.sleep(T)
    elem = driver.find_element(By.XPATH, '//*[@id="login-username"]')
    elem.send_keys(uname)
    elem = driver.find_element(By.XPATH, '//*[@id="login-password"]')
    elem.send_keys(pword)

    elem = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    elem.click()

    # Go to playlist
    time.sleep(T)
    driver.get("https://open.spotify.com/playlist/5RtFutweUW2ikVTADpa5Vq")
    time.sleep(T*5)

    # Accept cookies
    elem = driver.find_element(By.XPATH, "//*[@id=\"onetrust-accept-btn-handler\"]")
    elem.click()
    time.sleep(T)

    elem = driver.find_element(By.XPATH, "//*[@id=\"device-picker-icon-button\"]")
    elem.click()
    
    time.sleep(T*2)
    # Connect to FM Mansion
    try:
        elem = driver.find_element(By.CSS_SELECTOR, "button[aria-label='FB-Mansion undefined'")
        elem.click()
    except:
        print("FB Mansion already selected...")

    # Start playlist
    time.sleep(T*5)

    # Set volume TODO: FIX
    # elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[2]/footer/div[1]/div[3]/div/div[3]/div/div/div")
    # status = elem.get_attribute("style")
    # new_status = status[:25] + f"{0.1*100}%;"
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1])",elem, new_status)
    # elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[2]/footer/div[1]/div[3]/div/div[3]/div/div/div")
    # old_class = elem.get_attribute("class")
    # new_class = old_class + " DuvrswZugGajIFNXObAr"
    # driver.execute_script("arguments[0].setAttribute('class',arguments[1])",elem, new_class)

    # elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[2]/footer/div[1]/div[3]/div/div[3]/div/div/div")
    # status = elem.get_attribute("style")
    # new_status = status[:25] + f"{V*100}%;"
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1])",elem, new_status)

    # elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[2]/footer/div[1]/div[3]/div/div[3]/div/div/label/input")
    # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",elem, V)
    time.sleep(T)

    # Start first song in playlist
    elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button")
    elem.click()
    # Skip to next random song
    elem = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div[2]/footer/div[1]/div[2]/div/div[1]/div[2]/button[1]")
    elem.click()

    time.sleep(1*60)
    driver.close()
