from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

dept_name = ' '.join(sys.argv[1:-1])
c_number = str(sys.argv[-1])
print (dept_name, c_number)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://nubanner.neu.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search')

drop_down = driver.find_element_by_id('s2id_txt_term')

driver.implicitly_wait(2)
drop_down.click()
ta = driver.find_element_by_id('s2id_autogen1_search')

driver.implicitly_wait(2)
ta.send_keys("Spring 2020 Semester")

driver.implicitly_wait(5)
to_click = driver.find_element_by_id('202030')
to_click.click()

driver.implicitly_wait(2)
button = driver.find_element_by_id('term-go')
button.click()

driver.find_element_by_id('s2id_txt_subject').click()

# driver.implicitly_wait(2)
# drop_down.click()
ta = driver.find_element_by_id('s2id_autogen1')

driver.implicitly_wait(2)
if dept_name == 'DS':
    ta.send_keys("Data Science")
elif dept_name == 'CS':
    ta.send_keys("Computer Science")
elif dept_name == 'INFO':
    ta.send_keys("Information Systems Program")
elif dept_name == 'EM':
    ta.send_keys("Engineering Management")
elif dept_name == 'CSYE':
    ta.send_keys("Computer Systems Engineering")



driver.implicitly_wait(7)
if dept_name == 'DS':
    to_click = driver.find_element_by_id('DS')
elif dept_name == 'CS':
    to_click = driver.find_element_by_id('CS')
elif dept_name == 'INFO':
    to_click = driver.find_element_by_id('INFO')
elif dept_name == 'EM':
    to_click = driver.find_element_by_id('EMGT')
elif dept_name == 'CSYE':
    to_click = driver.find_element_by_id('CSYE')




to_click.click()

course_number = driver.find_element_by_id('txt_courseNumber')
course_number.send_keys(c_number)
driver.implicitly_wait(2)

driver.find_element_by_id('search-go').click()

table = driver.find_element_by_id('table1').find_element_by_tag_name('tbody')
rows = table.find_elements_by_tag_name("tr")
for r in rows:
    col = r.find_elements(BY.TAG_NAME, 'td')
    print (col.text)
# text = driver.find_element_by_xpath('//*[@id=\"table1\"]/tbody/tr[1]/[@data-property=\"status\"]')

driver.close()