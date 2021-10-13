from selenium import webdriver
from time import sleep
import json
#from selenium.webdriver.Chrome.options import Options

#options = Options()
#options.headless = True
driver = webdriver.Chrome()#options = options)
#driver.get('https://www.jiashu.dev')
#sleep(5)
test_login_data = ''
with open('jp_stock_data.json', 'r') as f:
    test_login_data = json.load(f)

driver.get('https://www.sbisec.co.jp/ETGate')

loginid_html = driver.find_element_by_name('user_id')
passwd_html = driver.find_element_by_name('user_password')
#TODO input needed for login id and password
loginid_html.send_keys(test_login_data['user'])
passwd_html.send_keys(test_login_data['pwd'])

login_click = driver.find_element_by_name('ACT_login')
login_click.click()
sleep(5)
#driver.get('https://site3.sbisec.co.jp/ETGate/')


ticker_input = driver.find_element_by_id('codeSearch')
ticker_input.send_keys('Sony')

ticker_search_click = driver.find_element_by_xpath(".//input[@alt='検索' and @type='image' and @src='https://sbisec.akamaized.net/sbisec/images/base02/btn-search-01.gif']")

ticker_search_click.click()

sleep(5)

buy_buttom = driver.find_elements_by_link_text('現物買')#.find_element_by_xpath(".//a[@href='/ETGate/?_ControlID=WPLETstT002Control&_DataStoreID=DSWPLETstT002Control&_PageID=DefaultPID&getFlg=on&_ActionID=DefaultAID&stock_sec_code=6758&market=TKY&stock_sec_code_mul=6758&_SeqNo=1634165214333_default_task_1381_WPLETsiR001Iser10_clickToSearchStockPriceJP&mktlist=TKY&trade_Market=']")
sell_buttom = driver.find_elements_by_link_text('現物売')#find_element_by_xpath(".//a[@href='/ETGate/?_ControlID=WPLETstT004Control&_DataStoreID=DSWPLETstT004Control&_PageID=DefaultPID&getFlg=on&_ActionID=DefaultAID&stock_sec_code=6758&market=TKY&stock_sec_code_mul=6758&_SeqNo=1634165214333_default_task_1381_WPLETsiR001Iser10_clickToSearchStockPriceJP&iscontrol1=1&mktlist=TKY&trade_Market=']")

#buy_buttom[0].click()
sell_buttom[0].click()
sleep(5)

driver.close()
