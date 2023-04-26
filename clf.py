import json
import undetected_chromedriver as uc
import time
import jmespath
from selenium.webdriver.common.by import By


def get():
    options = uc.ChromeOptions()

    options.user_data_dir = "c:\\temp\\profile"
    options.headless = True

    driver = uc.Chrome(
        options=options
    )

    driver.get("https://radiotech.su/api/")
    time.sleep(5)
    a = driver.find_element(By.TAG_NAME, "pre")
    a = a.text


    driver.close()
    driver.quit()
    # f = open("test.json")
    # a = f.read()
    # f.close

    a = json.loads(a)
    a = jmespath.search(f"[?course == `2`].groups",a)
    a = jmespath.search(f"[0][?name == 'Ис-261']",a)



    return(a)

