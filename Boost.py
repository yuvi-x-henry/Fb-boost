# same_id_fb_bot.py - TARGET = LOGIN ACCOUNT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

EMAIL = "henryinxide786@gmail.com"      # 👈 WO ID JO BOOST KARNA HAI
PASSWORD = "#HENRY#INXIDE#786"    # 👈 USI KA PASSWORD

TARGET_POSTS = [               # Multiple posts boost kar
    "https://www.facebook.com/61564155712159/posts/122168460608471857/?substory_index=1510473873314619&app=fbl",
    "https://facebook.com/POST2_ID", 
    "https://facebook.com/POST3_ID"
]

def run_pentest():
    options = Options()
    options.add_argument("--user-data-dir=./target_profile")  # Persistent TARGET profile
    driver = webdriver.Chrome(options=options)
    
    # STEP 1: TARGET ID LOGIN
    print("🔐 Logging into TARGET ID...")
    driver.get("https://facebook.com")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.ID, "pass").send_keys(PASSWORD)
    driver.find_element(By.NAME, "login").click()
    time.sleep(10)
    
    # STEP 2: SELF-LIKE/SELF-COMMENT (Normal activity)
    for post_url in TARGET_POSTS:
        print(f"🚀 Boosting: {post_url}")
        driver.get(post_url)
        time.sleep(5)
        
        # LIKE (if not already liked)
        try:
            like_btn = driver.find_element(By.XPATH, "//div[@aria-label='Like']")
            if "Unlike" not in like_btn.get_attribute("aria-label"):
                like_btn.click()
                print("✅ SELF-LIKE")
        except:
            print("⚠️ Already liked")
        
        time.sleep(random.uniform(2, 5))
        
        # COMMENT
        try:
            comment_box = driver.find_element(By.XPATH, "//div[@aria-label='Write a comment...']")
            comment_box.click()
            comments = ["🔥", "Great!", "👏", "Love it!", "💯"]
            comment_box.send_keys(random.choice(comments))
            comment_box.send_keys(u'\ue007')
            print(f"✅ SELF-COMMENT: {random.choice(comments)}")
        except:
            print("❌ Comment failed")
        
        time.sleep(random.uniform(10, 20))  # Natural gap
    
    print("🎯 PENTEST COMPLETE - TARGET BOOSTED!")
    time.sleep(60)
    driver.quit()

run_pentest()
