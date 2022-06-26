# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# For W3C actions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

import pytest

def testar_my_demo_app():
    ambiente = 'saucelabs'

    if ambiente == 'saucelabs':
        caps = {
            "platformName": "Android",
            "appium:platformVersion": "9.0",
            "appium:automationName": "Samsung Galaxy S9 FHD GoogleAPI Emulator",
            "appium:deviceOrientation": "portrait",
            "appium:app": "storage:filename=mda-1.0.13-15.apk",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        }

        driver = webdriver.Remote(
            "https://safiracamilo:f9165feb-cb9a-4d2d-94b0-e67e36893a76@ondemand.eu-central-1.saucelabs.com:443/wd/hub",
            caps)
    else:
        caps = {
            "platformName": "Android",
            "appium:plafformVersion": "9.0",
            "appium:appiumVersion": "1.22.3",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "emulador5554",
            "appium:deviceOrientation": "portrait",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActiivity"
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sauce Lab Back Packs")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    el2.click()
    #el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="View menu")
    #el3.click()

    #el4.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Gray color")
    el3.click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(572, 309)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(661, 296)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(505, 422)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(532, 392)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(462, 362)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(226, 169)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Increase item quantity")
    el4.click()

    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
    el5.click()

    el6 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartTV")
    el6.click()

    el7 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/totalPriceTV")
    el7.click()

    driver.quit()
