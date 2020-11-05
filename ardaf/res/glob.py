import sys

window_size = 1900, 1060
test_profile_url = "https://www.facebook.com/tuna.gul.1238"

driver_path = "ardaf/res/webdriver/chromedriver_"
driverpath = f"{driver_path}win32/chromedriver.exe" if sys.platform.startswith("win") else f"{driver_path}linux64/chromedriver"
