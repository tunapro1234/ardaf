import sys

window_size = 1900, 1060
test_profile_url = "https://www.facebook.com/tuna.gul.1238"

driver_path = "ardaf/res/webdriver/chromedriver_"
driverpath = f"{driver_path}win32/chromedriver.exe" if sys.platform.startswith("win") else f"{driver_path}linux64/chromedriver"

class PostModes:
    relative_id = "relative_id"
    relative_path = "relative_path"

post_modes = [PostModes.relative_id, PostModes.relative_path]

json_path = "ardaf/res/profile/profile.json"
default_profile = {
    "index": 0,
    "url": "tuna.gul.1238",
    "email": "tunagul54@gmail.com",
    "password": "tunapro1234",
}
