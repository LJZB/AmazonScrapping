import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def usd_to_cop(n):
    """Function to convert from USD to COP"""
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    currency = float(data['rates']['COP'])
    return round(n * currency, 2)


def calculate_values(driver, product_name):
    """This function takes the selenium driver, the url
    and the product name that is going to be searched.
    Then returns the three value components: price, shipping and
    import fees
    """
    driver.get("https://www.amazon.com/")
    # driver.maximize_window()  # Use for headful mode

    # Using the search box to filter by item name
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)

    # Opening the new item page to find the related price
    item = driver.find_element(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    item.click()

    # Clicking on the details tag
    details = driver.find_element(By.XPATH, "//span[@class='a-size-base' and text()=' Details ']")
    details.click()

    # Price, Shipping and Import Fees
    price = driver.find_element(By.XPATH, '//*[@id="a-popover-content-2"]/table/tbody/tr[1]/td[3]/span')
    price = price.text
    price = price.replace("$", "")
    price = float(price)
    price = usd_to_cop(price)

    shipping = driver.find_element(By.XPATH, '//*[@id="a-popover-content-2"]/table/tbody/tr[2]/td[3]/span')
    shipping = shipping.text
    shipping = shipping.replace("$", "")
    shipping = float(shipping)
    shipping = usd_to_cop(shipping)

    fees = driver.find_element(By.XPATH, '//*[@id="a-popover-content-2"]/table/tbody/tr[3]/td[3]/span')
    fees = fees.text
    fees = fees.replace("$", "")
    fees = float(fees)
    fees = usd_to_cop(fees)

    return price, shipping, fees


def data_extractor():
    pass
