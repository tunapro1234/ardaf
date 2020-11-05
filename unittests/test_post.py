from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

import ardaf.res.glob as glob
import unittest


class TestPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=glob.driver_path)
        self.input_text = "tunapro1234"
    
    def tearDown(self):
        self.driver.quit()
    
    def start(self):
        self.driver.get(glob.test_profile_url)
        self.driver.set_window_size(*glob.window_size)
        
        # self.driver.execute_script("window.scrollTo(0,150)")
        # self.driver.execute_script("window.scrollTo(0,344)")
        
        self.driver.execute_script("window.scrollTo(0, 500)")

    def test_post_relative_id(self):
        self.start()
        # yapf: disable
        self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[3]/div/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div/span").click()
        element = self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/form/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"ovfl\" data-offset-key=\"cp8ig-0-0\"><div data-offset-key=\"cp8ig-0-0\" class=\"_1mf _1mj\"><span data-offset-key=\"cp8ig-0-0\"><span data-text=\"true\">" + self.input_text + "</span></span></div></div></div>'}", element)
        self.driver.find_element(By.XPATH, "//div[@id=\'mount_0_0\']/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/form/div/div/div/div/div[3]/div[2]/div").click()
        #yapf: enable

    def test_post_relative_path(self):
        self.start()
        #yapf: disable
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/div/div/div/div/span").click()
        element = self.driver.find_element(By.XPATH, "//form/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"ovfl\" data-offset-key=\"cp8ig-0-0\"><div data-offset-key=\"cp8ig-0-0\" class=\"_1mf _1mj\"><span data-offset-key=\"cp8ig-0-0\"><span data-text=\"true\">" + self.input_text + "</span></span></div></div></div>'}", element)
        self.driver.find_element(By.XPATH, "//form/div/div/div/div/div[3]/div[2]/div").click()
        #yapf: enable
