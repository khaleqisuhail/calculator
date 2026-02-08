from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Chrome options ayarla
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=600,800")

try:
    # WebDriver başla
    driver = webdriver.Chrome(options=chrome_options)
    
    # HTML dosyasını aç
    file_path = "file:///d:/github%20repositories/calculator/site.html"
    driver.get(file_path)
    
    # Sayfanın yüklenmesini bekle
    time.sleep(2)
    
    # Tam sayfa screenshot'ı al
    driver.save_screenshot("images/calculator_full.png")
    print("✅ Full screenshot alındı: images/calculator_full.png")
    
    # Sadece hesap makinesi grid'i screenshot'ı al
    calculator_grid = driver.find_element(By.CLASS_NAME, "calculator-grid")
    calculator_grid.screenshot("images/calculator_interface.png")
    print("✅ Interface screenshot alındı: images/calculator_interface.png")
    
    # Sayı bas - "5" butonuna tıkla
    buttons_5 = driver.find_elements(By.ATTR, "data-Number")
    buttons = driver.find_elements(By.CSS_SELECTOR, "[data-Number]")
    
    # 5 butonunu bul
    for btn in buttons:
        if btn.text == "5":
            btn.click()
            break
    
    time.sleep(0.5)
    driver.save_screenshot("images/calculator_with_number.png")
    print("✅ Sayı girişi screenshot'ı alındı: images/calculator_with_number.png")
    
    # Toplama işlemi yap
    operation_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-operation]")
    for btn in operation_buttons:
        if btn.text == "+":
            btn.click()
            break
    
    time.sleep(0.5)
    driver.save_screenshot("images/calculator_with_operation.png")
    print("✅ İşlem screenshot'ı alındı: images/calculator_with_operation.png")
    
    driver.quit()
    print("\n✅ Tüm screenshot'lar başarıyla kaydedildi!")
    
except Exception as e:
    print(f"❌ Hata oluştu: {e}")
    print("Not: Chrome WebDriver'ın yüklü olması gerekmektedir.")
    print("Yüklemek için: pip install selenium")
