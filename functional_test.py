
from  selenium import webdriver
import unittest 
import time
from selenium.webdriver.common.keys import Keys 

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
    def tearDown(self):
        self.browser.quit()
    
    def test_can_a_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Todo list',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),'Enter a todo item'
        )
        inputbox.send_keys('Buy a car')
        time.sleep(1)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: buy a car ' for row in rows), 'you don`t buy a car xd'
        )
        self.fail("end test")


if __name__=='__main__':
    unittest.main(warnings='ignore')



