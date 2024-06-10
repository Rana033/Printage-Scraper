from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # choose selector


########################################
website = 'https://printige.net/'


driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website)
elements = driver.find_elements(By.CSS_SELECTOR, ".woocommerce-LoopProduct-link.woocommerce-loop-product__link")
books=[{"title":element.text,"link":element.get_attribute('href')}for element in elements]
print (books[0])

driver.quit()



 
