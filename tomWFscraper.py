from selenium import webdriver import time
from selenium.webdriver.common.keys import Keys
# http://selenium-python.readthedocs.io/index.html

def get_chase_amazon_driver(username, password):

    driver = webdriver.Chrome()
    driver.get("http://www.wellsfargo.com")

    time.sleep(2)
    
    WFUserName = driver.find_element_by_name("j_username")
    WFU.send_keys(username)
    WFPassword = driver.find_element_by_id("j_password")
    WFPassword.send_keys(password)

    WFPassword.submit()
    return driver
# Returns a logged-in Wells Fargo user/passowrd driver instance.
#
# HTML CODE FROM WELLS FARGO <input type="password" accesskey="P" id="password" name="j_password" maxlength="14">
# send_keys - sends string as keyboard output to 
# HTML CODE FROM WELLS FARGO <input type="text" accesskey="U" id="userid" name="j_username" maxlength="14" value="">
# http://selenium-python.readthedocs.io/locating-elements.html#locating-elements





def _goto_link(driver, text):
# Follow a link with a WebDriver
    l = driver.find_element_by_partial_link_text(text)
    driver.get(l.get_attribute('href'))


def get_recent_activity_rows(chase_driver):
# Return the 25 most recent CC transactions, plus any pending transactions.
# Returns: A list of lists containing the columns of the Chase transaction list.

    _goto_link(chase_driver, "See activity")
    time.sleep(10)

    rows = chase_driver.find_elements_by_css_selector("tr.summary")
    trans_list = []

    for row in rows:
        tds = row.find_elements_by_tag_name('td')
        tds = tds[1:]  # skip the link in first cell
        trans_list.append([td.text for td in tds])

    return trans_list


def get_activity(username, password):
# For a given username, retrieve recent account activity for a Chase CC
    rows = None
    d = get_chase_amazon_driver(username, password)
    time.sleep(8)

    try:
        rows = get_recent_activity_rows(d)
    except Exception, e:
        print e
    finally:
        d.quit()

    return rows

if __name__ == '__main__':
    import getpass

    uname = raw_input("Username: ")
    pwd = getpass.getpass()

    print get_activity(uname, pwd)
