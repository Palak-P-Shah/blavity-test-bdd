from Navigation_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def verify_load_more_stories():
    load_more = driver.find_element(By.XPATH, "(//button[normalize-space()='load more stories'])[1]")
    actions.move_to_element(load_more).perform()
    load_more.click()
    time.sleep(2)
    # after the button is clicked, now there are 8 news stories.
    number_of_articles = driver.find_elements(By.CLASS_NAME, "category-link-container")
    print("", len(number_of_articles))
    print("After clicking load more stories, number of articles present are: ", len(number_of_articles))


def post_click_load_more_verify_story(page_value):
    if page_value == "Op-Eds":
        page_value = "Opinion"
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='" + page_value + "']")))
    temp_string = "5"
    temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[" + temp_string + \
                 "]/div[2]/div[1]/div[2]/a[1]"

    by_xpath = "//div[" + temp_string + "]//div[2]//div[1]//div[3]//p[1]"
    header_xpath = "//div[" + temp_string + "]//div[2]//div[1]//div[1]//a[1]//p[1]"
    title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[" + temp_string + \
                  "]/div[2]/div[1]/div[2]/a[1]/span[1]"
    link = driver.find_element(By.XPATH, temp_xpath)
    by = driver.find_element(By.XPATH, by_xpath).text
    header = driver.find_element(By.XPATH, header_xpath).text
    title = driver.find_element(By.XPATH, title_xpath).text
    # print(driver.find_element(By.XPATH,by_xpath).text)
    # print(driver.find_element(By.XPATH, news_xpath).text)
    # print(driver.find_element(By.XPATH, title_xpath).text)
    if (by is not None) and by != "":
        print("By element is present for 5th article loaded after clicking load more stories")
    if (header is not None) and header != "":
        print("NEWS/OPINION/CULTURE element is present for 5th article loaded after clicking load more stories")
    if (title is not None) and title != "":
        print("title element is present for 5th article loaded after clicking load more stories")
    actions.move_to_element(link).perform()
    print("loaded link of blavity " + page_value + " : ", link.get_attribute('href'))
    blavity_page_link_url = link.get_attribute('href')
    if (blavity_page_link_url is None) or (blavity_page_link_url == ""):
        print("particular blavity " + page_value + " link is not there")
    driver.get(blavity_page_link_url)
    # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    print("Current window title for blavity story: " + driver.title)
    driver.back()
    print("After clicking load more button, the article link and page is displayed as expected")


def verify_each_story(page_value):
    count = 0
    time.sleep(2)
    while count < 4:
        if page_value == "Op-Eds":
            page_value = "Opinion"
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='"+page_value+"']")))
        temp_string = str(count + 1)
        temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[" + temp_string +\
                     "]/div[2]/div[1]/div[2]/a[1]"

        by_xpath = "//div[" + temp_string + "]//div[2]//div[1]//div[3]//p[1]"
        header_xpath = "//div[" + temp_string + "]//div[2]//div[1]//div[1]//a[1]//p[1]"
        title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[" + temp_string + \
                      "]/div[2]/div[1]/div[2]/a[1]/span[1]"
        link = driver.find_element(By.XPATH, temp_xpath)
        by = driver.find_element(By.XPATH, by_xpath).text
        header = driver.find_element(By.XPATH, header_xpath).text
        title = driver.find_element(By.XPATH, title_xpath).text
        # print(driver.find_element(By.XPATH,by_xpath).text)
        # print(driver.find_element(By.XPATH, news_xpath).text)
        # print(driver.find_element(By.XPATH, title_xpath).text)
        if (by is not None) and by != "":
            print("By element is present for this article")
        if (header is not None) and header != "":
            print("NEWS/OPINION/CULTURE element is present for this article")
        if (title is not None) and title != "":
            print("title element is present for this article")
        actions.move_to_element(link).perform()
        print("loaded link of blavity "+page_value+" : ", link.get_attribute('href'))
        blavity_page_link_url = link.get_attribute('href')
        if (blavity_page_link_url is None) or (blavity_page_link_url == ""):
            print("particular blavity "+page_value+" link is not there")
        driver.get(blavity_page_link_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title for blavity story: " + driver.title)
        driver.back()
        count += 1


def verify_news_page():
    page_value = "News"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    page.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories()
    post_click_load_more_verify_story(page_value)
    print("all the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_opinion_page():
    page_value = "Op-Eds"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    page.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories()
    post_click_load_more_verify_story(page_value)
    print("all the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_life_style_page():
    page_value = "Lifestyle"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    page.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories()
    post_click_load_more_verify_story(page_value)
    print("all the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_politics_page():
    page_value = "Politics"
    print("page is", page_value)
    time.sleep(2)
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    print("More link is active")
    more_page_link = driver.find_element(By.XPATH, "//a[normalize-space()='"+page_value+"']")
    more_page_link.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories()
    post_click_load_more_verify_story(page_value)
    print("all the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_culture_page():
    page_value = "Culture"
    print("page is", page_value)
    time.sleep(2)
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    print("More link is active")
    more_page_link = driver.find_element(By.XPATH, "//a[normalize-space()='"+page_value+"']")
    more_page_link.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories()
    post_click_load_more_verify_story(page_value)
    print("all the links of blavity "+page_value+" section are working correctly, including load more button")


# environment()
# page_load()
# post_page_load_pop_up()
# verify_opinion_page()
# verify_news_page
# verify_life_style_page()
# verify_politics_page()
# verify_culture_page()
# verify_footer_presence()
# driver.quit()
