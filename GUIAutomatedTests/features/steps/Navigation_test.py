from home_page_test import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


def verify_nav_bar_presence():
    print("check whether nav bar is present or not")
    time.sleep(3)
    nav_bar = driver.find_element(By.XPATH, "//ul[@class='navbar-nav d-desktop-flex align-items-center']")
    print(nav_bar.text)
    if (nav_bar.text is not None) and (nav_bar.text != ""):
        print("Nav Bar is present")
        pass


def verify_nav_news_link():
    print("checking the News tab")
    news_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='News']")
    news_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("News - Blavity News"))
    print("Current Window Title for News Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_opinions_link():
    print("checking the Opinion link")
    opinion_ed_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='Op-Eds']")
    opinion_ed_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Opinion - Blavity News"))
    print("Current Window Title for Opinion Eds Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_lifestyle_link():
    print("checking the Lifestyle tab")
    life_style_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='Lifestyle']")
    life_style_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Lifestyle - Blavity News"))
    print("Current Window Title for Life Style Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_blavity_u_link():
    blavity_u_link = driver.find_element(By.XPATH, "//a[normalize-space()='BlavityU']")
    blavity_u_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Blavity U - Blavity News"))
    print("Current Window Title for Blavity U Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_submit_story():
    submit_a_story_link = driver.find_element(By.XPATH, "//a[normalize-space()='Submit a Story']")
    submit_a_story_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    print("Current Window Title for Submit a Story is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_sign_up_link():
    sign_up_link = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    sign_up_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.url_to_be("https://join.blavity.com/"))
    print("Current window title for Sign Up is: " + driver.title)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("link for Sign Up Section is present and working as expected")


def verify_nav_search_bar():
    search_bar = driver.find_element(
        By.CSS_SELECTOR,
        "button[class='btn btn--search bg-transparent border-0 text-right text-white position-absolute']")
    search_bar.click()
    input_search = driver.find_element(By.XPATH, "//input[@type='text']")
    search_text = "culture"
    input_search.send_keys(search_text)
    search_bar.click()
    WebDriverWait(driver, 40).until(ec.url_contains(search_text))
    WebDriverWait(driver, 40).until(ec.title_is("Search - Blavity News"))
    print("Current window title for Search Page is: " + driver.title)
    print("link for Search is present and working as expected")


def verify_nav_more_section():
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    print("More link is active")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//h1[contains(text(),'Blavity News is a community and platform for Black')]")))
    more_link_email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    more_link_email.send_keys("test@gmail0.com")
    more_link_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    more_link_checkbox.click()
    submit_more_email_link = driver.find_element(By.XPATH, "//button[normalize-space()='submit']")
    submit_more_email_link.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//p[@class='success-message text-silver']")))
    success_msg_on_click = driver.find_element(By.XPATH, "//p[@class='success-message text-silver']")
    if (success_msg_on_click.text is not None) and (success_msg_on_click.text != ""):
        print("Email section of more link is working as expected")
    more_politics_link = driver.find_element(By.XPATH, "//a[normalize-space()='Politics']")
    more_politics_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Politics - Blavity News"))
    # print("Current Window Title for Politics is : ", driver.title)
    print("Link for Politics under More Section is working as expected")
    more_link.click()
    more_news_link = driver.find_element(By.XPATH, "//a[normalize-space()='News']")
    more_news_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("News - Blavity News"))
    # print("Current Window Title for Politics is : ", driver.title)
    print("Link for News under More Section is working as expected")
    more_link.click()
    more_op_ed_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Op-Eds']")
    more_op_ed_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Opinion - Blavity News"))
    # print("Current Window Title for Politics is : ", driver.title)
    print("Link for Op-Eds under More Section is working as expected")
    more_link.click()
    more_write_a_story_link = driver.find_element(By.XPATH, "//a[normalize-space()='Write a Story']")
    more_write_a_story_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Write a Story under More Section is working as expected")
    more_link.click()
    more_terms_link = driver.find_element(By.XPATH, "//a[normalize-space()='Terms & Conditions']")
    more_terms_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Terms & Conditions under More Section is working as expected")
    more_link.click()
    more_partner_with_us_link = driver.find_element(By.XPATH, "//a[normalize-space()='Partner With Us']")
    more_partner_with_us_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Partner With Us under More Section is working as expected")
    more_link.click()
    more_culture_link = driver.find_element(By.XPATH, "//a[normalize-space()='Culture']")
    more_culture_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Culture - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Culture under More Section is working as expected")
    more_link.click()
    more_my_account_link = driver.find_element(By.XPATH, "//a[normalize-space()='My Account']")
    more_my_account_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for My Account under More Section is working as expected")
    driver.back()
    more_link.click()
    more_careers_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Careers']")
    more_careers_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Careers under More Section is working as expected")
    more_link.click()
    more_life_style_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Lifestyle']")
    more_life_style_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Lifestyle - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for LifeStyle under More Section is working as expected")
    more_link.click()
    more_privacy_policies_link = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy Policies']")
    more_privacy_policies_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Privacy Policy under More Section is working as expected")
    more_link.click()
    more_shop_link = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")
    more_shop_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Shop under More Section is working as expected")
    more_link.click()
    more_social_justice_link = driver.find_element(By.XPATH, "//a[normalize-space()='Social Justice']")
    more_social_justice_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Social Justice under More Section is working as expected")
    more_link.click()
    more_mastercard_link = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity x Mastercard']")
    more_mastercard_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Blavity x Mastercard under More Section is working as expected")
    news_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='News']")

    news_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("News - Blavity News"))

    # more_text = driver.find_element(
    #     By.XPATH, "//h6[contains(text(),'Blavity is a community of the most exceptional mul')]")
    # actions.move_to_element(more_text)
    # more_instagram_link = driver.find_element(
    # By.XPATH, "//header[@class='app-header bg-black position-sticky']//div[@class='d-desktop-none']//a[1]")
    # # more_instagram.location_once_scrolled_into_view
    # more_link.click()
    # WebDriverWait(driver, 40).until(
    #     ec.presence_of_element_located((By.XPATH,
    #     "//header[@class='app-header bg-black position-sticky']//div[@class='d-desktop-none']//a[1]")))
    # #
    # # time.sleep(2)
    # more_instagram_link.click()
    # # more_instagram
    # verify_blavity_footer_instagram()


def verify_nav_bar_links():
    print("check whether each nav bar link is present and working, total 7 links")
    verify_nav_news_link()
    verify_nav_opinions_link()
    verify_nav_lifestyle_link()
    verify_nav_blavity_u_link()
    verify_submit_story()
    verify_sign_up_link()
    verify_nav_search_bar()
    print("All 7 links :- News, Op-Eds, Lifestyle, BlavityU, Submit a "
          "Story, Sign-Up and search bar are working as expected.")
    verify_nav_more_section()


def verify_footer_presence():
    time.sleep(3)
    footer_news_page = driver.find_element(By.XPATH,
                                           "//footer[@class='app-footer text-center text-desktop-left text-white']")
    actions.move_to_element(footer_news_page).perform()
    if footer_news_page.is_displayed() is True:
        print("footer section is displayed on news page")


def exit_browser():
    print("closing the browser instance")
    driver.quit()
