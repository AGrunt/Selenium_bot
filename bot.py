import time
import polling2
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

#print("Pick a service to scratch")
#print(f"1: Facebook Ad Library")
#print(f"2: TikTok Ad Library")
#user_choice = input('Choice wisely: ')

#if user_choice not in ['1', '2']:
#    user_choice = input('Choice must be 1 or 2: ')
#else:
#    user_choice = int(user_choice) - 1

services = {
    'service_Name': ['Facebook Ad Lybrary', 'TikTok Ads Library'],
    'service_URL': ['https://www.facebook.com/ads/library/', 'https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=30&region=AU']
    }

chrome_options = Options()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--window-size=1000,800")
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension('./assets/IJKBMHMJNBODJFGHDBDHPNOLCDANFBFN_1_1_0_0.crx')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
                                
driver.get("chrome://extensions/?id=ijkbmhmjnbodjfghdbdhpnolcdanfbfn")
driver.execute_script("return document.querySelector('extensions-manager').shadowRoot.querySelector('#viewManager > extensions-detail-view.active').shadowRoot.querySelector('div#container.page-container > div.page-content > div#options-section extensions-toggle-row#allow-incognito').shadowRoot.querySelector('label#label input').click()");

def open_service(service, url):
    driver.get(url)
    polling2.poll(lambda: driver.find_element(By.XPATH, "//*[contains(text(), 'Save to HeyStak')]"), step=0.5, poll_forever=True, ignore_exceptions = (NoSuchElementException))
    time.sleep(5)
    print(f"Service: {service}")
    return

#statistics if we reach end of the internet and were not droped by facebook or tiktok.
def stats(service, total_ads, total_pages, elapsewd_time):
    print(f'{service} scratching statistics:')
    print(f'Total ads count: {total_ads}')
    print(f'Total pages count: {total_pages}')
    print(f'Elapsed time: {elapsewd_time}')
    return

#clicker
def click_them_all(user_choice):
    # Get scroll height
    last_height = 400
    start = datetime.now()
    while True:
        for btn in driver.find_elements(By.CLASS_NAME, "btn-primary"):
            if btn.is_enabled() and btn.is_displayed():
                print(f'btn: {btn}')
                btn.click()
                time.sleep(5)
        # Scroll down to bottom
        driver.execute_script(f"window.scrollTo(0, {last_height});")
        # Wait to load page
        time.sleep(4)
        # Calculate new scroll height and compare with last scroll height
        new_height = last_height + 400 
        if new_height == last_height:
            print(f'I have reach the end of the internet. it took {datetime.now() - start}')

            break
        last_height = new_height        
    return
#==================================================================

open_service(services['service_Name'][0],services['service_URL'][0])
click_them_all(0)

#uncomment once tiktok unlocked.
#open_service(services['service_Name'][user_choice],services['service_URL'][user_choice])
#click_them_all(user_choice)