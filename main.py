# Importing libraries
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from functions import calculate_values

try:
    # Driver options
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Edge(options=options)
    (price, shipping, fees) = calculate_values(driver, "i5-13400")

    total = price + shipping + fees

    print(f'Precio = {"{:,}".format(price)}'
          , f'Envío = {"{:,}".format(shipping)}'
          , f'Impuestos = {"{:,}".format(fees)}'
          , f'Total = {"{:,}".format(total)}'
          , sep='\n')
except Exception as e:
    print("Excepción encontrada: " + repr(e))

finally:
    driver.quit()
