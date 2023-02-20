from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://vernik.me/'
broweser = webdriver.Chrome()
broweser.maximize_window()
broweser.get(link)

search_string = broweser.find_element(By.CSS_SELECTOR, "input[class*=search-form__input]")
search_string.send_keys("Iphone 13 pro max")
knopka = broweser.find_element(By.CSS_SELECTOR, "button[class*=search-form__button_search]").click()

proverka = WebDriverWait(broweser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=catalog__title]"))).text
proverka1 = 'Поиск “Iphone 13 pro max”'
assert proverka == proverka1, f"Тест не пройден, вот что получилось{proverka1}"

broweser.quit()