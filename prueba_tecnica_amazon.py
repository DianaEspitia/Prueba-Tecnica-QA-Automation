from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Seleccionar el navegador
print('Seleccione el navegador que desea utilizar')
print('1. Google Chrome')
print('2. Firefox')
print()
buscador = int(input('Buscador: '))

if buscador == 1:
    driver = webdriver.Chrome()
elif buscador == 2:
    driver = webdriver.Firefox()
else:
    print('Ingresó un valor incorrecto')
    exit()

driver.maximize_window()
driver.get('https://www.amazon.com/') #Abrir página de Amazon

#Búsqueda de artículo
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('consola de videojuegos')
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

#Espera 
wait = WebDriverWait(driver,10)
bandera = '//*[@id="deliveryRefinements"]'

try:
    wait.until(ec.visibility_of_element_located((By.XPATH, bandera)))
except Exception as e:
    print("Fallas en la prueba, el elemento indicado (bandera) no fue encontrado.")
    print()
    print(str(e))
    exit()

#Elección de artículo    
try:
    images = driver.find_elements(By.CLASS_NAME, 's-image')
    images[1].click()
except Exception as e2:
    print("Fallas en la prueba, el articulo indicado no fue encontrado.")
    print()
    print(str(e2))
    exit()
    
#Esperar a que se encuentre el botón para agregar el carrito de compras
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]'))) 
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()
except Exception as e3:
    print("Fallas en la prueba. El botón para agregar el artículo al carrito de compras no se encontró, esto puede ser porque el producto seleccionado no se encuentra disponible.")
    print()
    print(str(e3))
    exit()

#Ver carrito
driver.find_element(By.XPATH, '//*[@id="nav-cart"]').click()

##----------------------------------------------------------------------------------------------------------------------
##Checkout
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input'))) 
    driver.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input').click()
except Exception as e3:
    print("Fallas en la prueba. El botón para proceder con el pago no se encontró, esto puede ser porque el producto seleccionado no se encuentra disponible.")
    print()
    print(str(e3))
    exit()

#Iniciar Sesión - Correo
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ap_email"]')))
    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('mail')
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="continue"]')))
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
except Exception as e4:
    print("Fallas en la prueba. Inicio de sesión - correo.")
    print()
    print(str(e4))
    exit()

#Iniciar Sesión - Contraseña
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ap_password"]')))
    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('password')
    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()
except Exception as e4:
    print("Fallas en la prueba. Inicio de sesión - contraseña.")
    print()
    print(str(e4))
    exit()

#Dirección de envío
menu = '//*[@id="address-ui-widgets-countryCode"]' 
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="address-ui-widgets-enterAddressFormContainer"]/h2')))
    #wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="address-ui-widgets-enterAddressFormContainer"]/h2')))
    
    driver.find_element(By.XPATH, menu).click()
    driver.find_element(By.XPATH, '//*[@id="1_dropdown_combobox"]/li[46]/a').click()   
   
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-enterAddressFullName"]').send_keys('Nombre Apellido')    
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-enterAddressLine1"]').send_keys('Dirección')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-enterAddressCity"]').send_keys('Ciudad')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-enterAddressPostalCode"]').send_keys(100000)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-enterAddressPhoneNumber"]').send_keys(1234567890)
    time.sleep(1)
    boton_direccion = driver.find_element(By.XPATH, '//*[@id="address-ui-widgets-form-submit-button"]/span/input').click()
    time.sleep(1)    
except Exception as e5:
    print("Fallas en la prueba. Dirección de envío.")
    print()
    print(str(e5))
    exit()

#Método de pago
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="apx-content"]/div/div[2]/div[2]/div[1]/h2')))
    driver.execute_script("window.scrollTo(0, 0)") 
    
    time.sleep(1)
    driver.find_element(By.NAME, 'ppw-instrumentRowSelection').click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.NAME, 'ppw-widgetEvent:SetPaymentPlanSelectContinueEvent')))
    driver.find_element(By.NAME, 'ppw-widgetEvent:SetPaymentPlanSelectContinueEvent').click()
    time.sleep(5)

except Exception as e6:
    print("Fallas en la prueba. Método de pago.")
    print()
    print(str(e6))
    exit()  

print("La prueba se ha completado con éxito")

driver.close()
