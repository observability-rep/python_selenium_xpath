#https://duckduckgo.com/?q=selenium+example+use+in+browser&va=i&t=hc&iar=videos&iax=videos&ia=videos&iai=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DSPM1tm2ZdK4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links =driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break


book_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(.,  '7 IN 1')]]][count(.//a)=2]//a")
for book_link in book_links:
    print(book_link.get_attribute("innerHTML"))

book_links[0].click()
driver.switch_to.window(driver.window_handles[1])
#time.sleep(6)
buttons =  driver.find_elements("xpath","//a[.//span[text()[contains(., 'Taschenbuch')]]]//span[text()[contains(.,  '€')]]")

for button in buttons:
    print(button.get_attribute("innerHTML").replace("&nbsp;", " "))