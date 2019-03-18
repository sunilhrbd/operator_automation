from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("/usr/local/chromedriver")
driver.maximize_window()
# get_url function
driver.get("http://operator.swoo.tv")

# login page details : REMOVE HARDCODED STRING AFTER TEST


driver.find_element_by_id("username").send_keys("sunilkumar")
driver.find_element_by_id("password").send_keys("sunilkumar@hushuqhsb")
login = driver.find_element_by_css_selector(".btn-lg")
login_hover = ActionChains(driver).move_to_element(login).click().perform()
time.sleep(5)
# opening a new tab to enter game url in a separate function
current_tab = driver.current_window_handle
driver.execute_script('window.open();')
new_tab = [tab for tab in driver.window_handles if tab != current_tab][0]
driver.switch_to.window(new_tab)

# function to get URL"""
#driver.get("http://stage-operator.swoo.tv/bingo/active-games?region=AF")
game_id = "fa4b1a74-ccbd-4c9b-aa74-80f476b3bd4a"
game_type= "candyrush"


def get_url(game_type,game_id):
    return "http://operator.swoo.tv/"+game_type+"/operator?gameid="+game_id+"&region=IN"

#http://stage-operator.swoo.tv/bingo/operator?gameid=06a21b89-c6a7-4304-8c17-5fdd5fbd1aff&region=IN

driver.get(get_url(game_type,game_id))

# driver.get("https://stage-operator.swoo.tv/bingo/operator?gameid=4421cc73-c5e3-4eef-9f9d-38c37a759ec6&region=IN")

time.sleep(10)
#10 round
if(game_type=="candyrush"):
    Prepare_game = driver.find_element_by_css_selector('#PREPARE > div:nth-child(2)')
    Prepare_game.click()
    time.sleep(2)
    Prepare_game.click()  # checking if the button is press
    time.sleep(120)  # change the sleep time here
    startBroadcast = driver.find_element_by_css_selector('#BROADCAST > div:nth-child(2)')
    startBroadcast.click()
    time.sleep(2)
    startBroadcast.click()
    time.sleep(30)
    generateCard = driver.find_element_by_css_selector('#CLAIM_CARD > div:nth-child(2)')
    generateCard.click()
    time.sleep(2)
    generateCard.click()
    time.sleep(44)
    startGameHost = driver.find_element_by_css_selector('#START_HOST > div:nth-child(2)')
    startGameHost.click()
    time.sleep(1)
    startGamePlayers = driver.find_element_by_css_selector('#START > div:nth-child(2)')
    startGamePlayers.click()
    time.sleep(2)
    startGamePlayers.click()
    time.sleep(916)
    CalculateWinners = driver.find_element_by_xpath('//*[@id="STOP_GAME"]/div[2]')
    CalculateWinners.click()
    time.sleep(2)
    displayWinners = driver.find_element_by_css_selector('#DISPLAY_WINNERS > div:nth-child(2)')
    displayWinners.click()
    time.sleep(28)
    stopFeed = driver.find_element_by_css_selector('#END > div:nth-child(2)')
    stopFeed.click()

elif(game_type=="bingo"):
    Prepare_game = driver.find_element_by_css_selector('#PREPARE > div:nth-child(2)')
    Prepare_game.click()
    time.sleep(2)
    Prepare_game.click()  # checking if the button is press
    time.sleep(120)  # change the sleep time here
    startBroadcast = driver.find_element_by_css_selector('#BROADCAST > div:nth-child(2)')
    startBroadcast.click()
    time.sleep(2)
    startBroadcast.click()
    time.sleep(30)
    generateCard = driver.find_element_by_xpath('//*[@id="CLAIM_CARD"]/div[2]')
    generateCard.click()
    time.sleep(2)
    generateCard.click()
    time.sleep(20)
    startGameHost = driver.find_element_by_xpath('//*[@id="START_HOST"]')
    startGameHost.click()
    time.sleep(26)
    startGamePlayers = driver.find_element_by_xpath('//*[@id="START"]/div[2]')#//*[@id="START"]/div[2]
    startGamePlayers.click()
    time.sleep(610)
    startGamePlayers.click()
    time.sleep(45)
        #CalculateWinners = driver.find_element_by_xpath('//*[@id="STOP_GAME"]/div[2]')
        #CalculateWinners.click()
        #time.sleep(10)
    displayWinners = driver.find_element_by_xpath('//*[@id="DISPLAY_WINNERS"]/div[2]')#//*[@id="DISPLAY_WINNERS"]/div[2]
    displayWinners.click()
    time.sleep(50)
    stopFeed = driver.find_element_by_xpath('//*[@id="END"]/div[2]')#//*[@id="END"]/div[2]
    stopFeed.click()


