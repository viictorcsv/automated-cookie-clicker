import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

if __name__ == '__main__':
    driver = uc.Chrome()

    try:
        driver.get("https://orteil.dashnet.org/cookieclicker/")

        cookie_id = "bigCookie"
        product_prefix = "product"
        upgrade_prefix = "upgrade"

        print("Aguardando seleção de idioma...")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
        ).click()

        cookie = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, cookie_id))
        )
        print("Jogo iniciado!")

        while True:

            for _ in range(150):
                try:
                    cookie.click()
                except:
                    pass
            
            try:

                upgrade = driver.find_element(By.ID, upgrade_prefix + "0")
                
                if "enabled" in upgrade.get_attribute("class"):
                    upgrade.click()
                    print(">>> UPGRADE COMPRADO!")
            except (NoSuchElementException, StaleElementReferenceException):
                pass

            for i in range(15, -1, -1):
                try:
                    product = driver.find_element(By.ID, product_prefix + str(i))
                    
                    product_class = product.get_attribute("class")
                    
                    if "enabled" in product_class:
                        product.click()
                        print(f"Produto {i} comprado!")
                        break
                        
                except (NoSuchElementException, StaleElementReferenceException):
                    continue

    except Exception as e:
        print(f"Erro fatal: {e}")
    
    finally:
        driver.quit()