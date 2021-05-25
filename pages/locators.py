from selenium.webdriver.common.by import By


class YandexPageLocators:

    LOCATOR_ENTER_BUTTON = (By.XPATH, "//a[contains(@class, 'desk-notif-card__login-new-item_enter')]")
    LOCATOR_USERNAME_INPUT = (By.ID, "passp-field-login")
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOCATOR_PASSWORD_INPUT = (By.XPATH, "//input[@name='passwd']")
    LOCATOR_MAIL_BUTTON = (By.XPATH, 
        "//div[@class='desk-notif-card__details']/descendant::div[contains(@class, 'desk-notif-card__mail-title')]")

class MailPageLocators:

    LOCATOR_MESSAGES_TITLE = (By.XPATH, 
        "//*[contains(@class,'mail-MessageSnippet-Item_subjectWrapper')]/child::span[contains(@class,'mail-MessageSnippet-Item_subject')]")
    LOCATOR_SEND_A_MESSAGE_BUTTON = (By.CSS_SELECTOR, '.mail-ComposeButton-Text')
    LOCATOR_TO_WHOM_INPUT = (By.XPATH, 
        "//div[contains(@class, 'ComposeRecipients-TopRow')]/descendant::div[contains(@class, 'MultipleAddressesDesktop-Field')]/child::div")
    LOCATOR_TITLE_INPUT = (By.XPATH, "//input[contains(@class, 'composeTextField')]")
    LOCATOR_MESSAGE_INPUT_FIELD = (By.XPATH, "//div[@role='textbox']")
    LOCATOR_SEND_BUTTON = (By.XPATH, 
        "//div[contains(@class, 'ComposeControlPanel-SendButton')]/descendant::button")