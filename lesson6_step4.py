from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, когда цена станет $100 (ожидаем до 15 секунд)
    price_element = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)
    
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получаем результат из алерта
    time.sleep(2)
    alert = browser.switch_to.alert
    result = alert.text
    print(f"Результат: {result}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
