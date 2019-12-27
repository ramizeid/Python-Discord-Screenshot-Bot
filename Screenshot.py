from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from PIL import Image

# Opens the website with the given url
url = "https://google.com"
screenshot_number = 0

driver = webdriver.Chrome(executable_path="CHROME DRIVER LOCATION/Python/Python37-32/Drivers/chromedriver.exe")
driver.maximize_window()

if url[0] != "h" and url[1] != "t" and url[2] != "t" and url[3] != "p" and url[4] != "s" and url[5] != ":" and url[6] != "/" and url[7] != "/":
    url = "https://" + url

driver.get(url)
element = driver.find_element_by_tag_name('html')

# Creates the screenhots
try:
    for i in range(10000):
        path = f"SCREENSHOT SAVE LOCATION/Screenshots/{screenshot_number}.png"
        driver.save_screenshot(path)
        if i != 0:
            previous_img = f"SCREENSHOT SAVE LOCATION/Screenshots/{screenshot_number - 1}.png"
            current_img = f"SCREENSHOT SAVE LOCATION/Screenshots/{screenshot_number}.png"

            if open(previous_img, "rb").read() == open(current_img, "rb").read():
                os.unlink(current_img)
                break

# Concatenates all of the small screenshots into one big image
        im1 = Image.open(f"SCREENSHOT SAVE LOCATION/Screenshots/0.png")
        dst = Image.new('RGB', (1920, 888 + 888 * i))
        dst.paste(im1, (0, 0))
        k = 1

        while k <= i:
            if k == i:
                # Fix this so that the final picture doesn't look like it's cut
                # Also make it so that it deletes all of the other screenshots and only keeps the final one
                # Change the name of the final screenshot to the id of the screenshot page
                dst.paste(Image.open(f"SCREENSHOT SAVE LOCATION/Screenshots/{k}.png"), (0, 850 * k))
                break
            dst.paste(Image.open(f"SCREENSHOT SAVE LOCATION/Screenshots/{k}.png"), (0, 850 * k))
            k += 1

        dst.save("SCREENSHOT SAVE LOCATION/Screenshots/Final_Picture.png")

        element.send_keys(Keys.DOWN * 17)
        screenshot_number += 1
        time.sleep(0.5)

except:
    print('Error: Task not completed.')

# Closes the browser
driver.quit()
