from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random

def sikayetvar_garanti(keywords):
    results = []
    
    print("--- ŞİKAYETVAR GARANTİLİ TOPLAYICI ---")
    print("Google üzerinden Şikayetvar linklerini topluyoruz.\n")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option('useAutomationExtension', False) 
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        for word in keywords:
            print(f"--> '{word}' aranıyor...")
            
            try:
                driver.get("https://www.google.com")
                time.sleep(2)
                
                search_box = driver.find_element(By.NAME, "q")
                # site:sikayetvar.com komutuyla sadece şikayetleri çağırıyoruz
                query = f'site:sikayetvar.com "{word}"'
                
                search_box.clear()
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)
                
                time.sleep(3)
                if "sorry" in driver.current_url or "recaptcha" in driver.page_source.lower():
                    print("\n!!! GOOGLE CAPTCHA !!! Lütfen çözün ve ENTER'a basın.")
                    input("Bekliyorum... > ")
                    time.sleep(2)
                
                
                all_links = driver.find_elements(By.TAG_NAME, "a")
                print(f"    (Sayfada toplam {len(all_links)} link tarandı...)")
                
                found_count = 0
                seen_urls = set()
                
                for link_element in all_links:
                    try:
                        href = link_element.get_attribute("href")
                        text = link_element.text # Linkin üzerindeki yazı (Başlık)
                        
                        if href and "sikayetvar.com" in href and "google" not in href:
                            if href not in seen_urls:
                                
                                if not text:
                                    text = "Başlık Alınamadı"
                                    
                                results.append({
                                    "Aranan Kelime": word,
                                    "Şikayet Başlığı": text,
                                    "Link": href
                                })
                                seen_urls.add(href)
                                found_count += 1
                    except:
                        continue
                
                print(f"    ✓ {found_count} adet şikayet bulundu.")
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                print(f"    ! Hata: {e}")

    except Exception as e:
        print(f"!!! GENEL HATA: {e}")
    
    finally:
        print("\n--- İŞLEM BİTTİ ---")
        
        if results:
            df = pd.DataFrame(results)
            dosya_adi = "sikayetvar_garanti_sonuc.xlsx"
            df.to_excel(dosya_adi, index=False)
            print(f"BAŞARILI! Dosya masaüstüne kaydedildi: {dosya_adi}")
            print(df.head())
        else:
            print("!!! HİÇ VERİ BULUNAMADI !!!")
            print("Sebebi Google CAPTCHA olabilir veya arama sonucunda reklam çıkmış olabilir.")
            
        print("\nProgram kapanmak için seni bekliyor.")
        input("Kapatmak için ENTER tuşuna bas...")
        driver.quit()

keywords = [
    "key word1",
    "key word2"
    ]

if __name__ == "__main__":
    sikayetvar_garanti(keywords)