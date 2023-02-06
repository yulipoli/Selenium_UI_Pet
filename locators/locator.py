from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    LOGO = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/div[1]/img[1]')
    SECOND_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/span/button[2]')
    THIRD_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/span/button[3]')
    LAST_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[4]')
    PREVIOUS_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[2]/span')
    NEXT_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[3]/span')
    FIRST_P = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[1]/span')
    COMMENT_FIELD = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[3]/form/div/div/div[2]/div[1]')
    SAVE_COMMENT_BTN = (By.CLASS_NAME, "p-button-label")
    PET_DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button/span')
    DROP_DOWN = (By.ID, "typesSelector")
    DD_DOG = (By.ID, "pv_id_2_0")
    DD_REPTILE = (By.ID, "pv_id_2_2")
    DD_HAMSTER = (By.ID, "pv_id_2_3")
    FILTER_FIELD = (By.ID, "petName")
    AMY_BTN = (By.CLASS_NAME, "p-button-label")
    DORI_BTN = (By.CLASS_NAME, "p-button-label")
    HEADER = (By.CLASS_NAME, "p-dataview-header")
    PET_PICTURE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]')
    CLOSE_BUTTON = (By.XPATH, '/html/body/div[3]/div[1]/button[5]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    QUIT_BTN = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[2]/a[1]/span[2]')
    ERROR_POPUP = (By.XPATH, 'body/div[2]/div[1]/div[1]/div[1]')


class ProfilePageLocators:
    PLUS_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    CREATE_NAME = (By.ID, "name")
    CREATE_AGE = (By.XPATH, '//*[@id="age"]/input')
    CREATE_TYPE = (By.ID, "typeSelector")
    TYPE_CAT = (By.CLASS_NAME, "p-dropdown-item")
    CREATE_GENDER = (By.ID, "genderSelector")
    GENDER_FEMALE = (By.CLASS_NAME, "p-dropdown-item")
    SUBMIT_BTN = (By.CLASS_NAME, "p-button-label")
    CHOOSE_BTN = (By.CLASS_NAME, "p-button-label")
    CHOOSE_UPL = (By.CLASS_NAME, "p-button p-component p-fileupload-choose")
    MENU_BAR = (By.CLASS_NAME, "card")
    PROFILE_BTN = (By.XPATH, "//div[@id='app']/header/div/ul/li/a")
    EDIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]/span[2]')
    EDIT_NAME = (By.ID, "name")
    EDIT_AGE = (By.XPATH, '//*[@id="age"]/input')
    EDIT_SAVE_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button/span[2]')
    YES_BTN = (By.XPATH, '/html/body/div[3]/div[2]/button[2]/span')
    NO_BTN = (By.TAG_NAME, 'span')
    DELETE_BTN = (By.XPATH, "//button[2]/span[2]")



