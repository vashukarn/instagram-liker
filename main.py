from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def login():
    driver.maximize_window()
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(10)
    print("Logging you into your account")
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
    sleep(1)
    try:
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    except Exception as e:
        print("Successfully logged in" + str(e))
    sleep(3)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()
    except Exception as e:
        print("Successfully logged in" + str(e))


def main():
    print('Starting to send likes to user')
    driver.get('https://www.instagram.com/' + user + '/')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()
    sleep(1)
    i = 0
    while i < num:
        driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        driver.save_screenshot('like' + str(i) + '.png')
        sleep(1)
        driver.find_element_by_class_name(
            'coreSpriteRightPaginationArrow').click()
        i += 1
        sleep(1)


# Enter your credentials here
print("Enter correct credentials to make this script work")
username = str(input('Enter your instagram username : '))
password = str(input('Enter your instagram password : '))

# Enter the posts you want to like here
user = str(input('Enter instagram id of user : '))
num = int(input('Enter no of posts you want to like : '))

print("Opening Chrome Browser...")

chrome_options = Options()

# Uncomment two lines down if you don't want chrome window to popup and go headless
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
login()
main()
driver.quit()
print(str(num) + ' posts of ' + user +
      ' liked and screenshots saved successfully. ')
