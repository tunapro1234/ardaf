from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

import ardaf.res.glob as glob
import unittest

küçük birfrom ardaf.res.glob import PostModes


class TestPost:
    def __init__(self, driver, input_text, mode=glob.post_modes[0]):
        if mode not in [*glob.post_modes, *range(len(glob.post_modes))]:
            raise ValueError("Post Mode Not Found...")

        self.mode = glob.post_modes[mode] if type(mode) is int else mode
        self.input_text = input_text
        self.driver = driver

    def __start(self):
        self.driver.get(glob.test_profile_url)
        self.driver.set_window_size(*glob.window_size)

        # self.driver.execute_script("window.scrollTo(0,150)")
        # self.driver.execute_script("window.scrollTo(0,344)")

        self.driver.execute_script("window.scrollTo(0, 500)")

    def __post_relative_id(self, input_text):
        # yapf: disable
        self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[3]/div/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div/span").click()
        element = self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/form/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"ovfl\" data-offset-key=\"cp8ig-0-0\"><div data-offset-key=\"cp8ig-0-0\" class=\"_1mf _1mj\"><span data-offset-key=\"cp8ig-0-0\"><span data-text=\"true\">" + input_text + "</span></span></div></div></div>'}", element)
        self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/form/div/div/div/div/div[3]/div[2]/div").click()
        #yapf: enable

    def __post_relative_path(self, input_text):
        #yapf: disable
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div/div/div/div/span").click()
        element = self.driver.find_element(By.XPATH, "//form/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"ovfl\" data-offset-key=\"cp8ig-0-0\"><div data-offset-key=\"cp8ig-0-0\" class=\"_1mf _1mj\"><span data-offset-key=\"cp8ig-0-0\"><span data-text=\"true\">" + input_text + "</span></span></div></div></div>'}", element)
        self.driver.find_element(By.XPATH, "//form/div/div/div/div/div[3]/div[2]/div").click()
        #yapf: enable

    def launch(self, input_text: str = None):
        input_text = self.input_text if input_text is None else input_text

        self.__start()

        if self.mode == glob.PostModes.relative_id:
            self.__post_relative_id(input_text)
        elif self.mode == glob.PostModes.relative_path:
            self.__post_relative_path(input_text)