from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    username_textbox_id = (By.ID, 'txtUsername')
    password_textbox_id = (By.ID, 'txtPassword')
    login_button_id = (By.ID, 'btnLogin')
    invalidUsername_message_id = (By.ID, 'spanMessage')


class HomePageLocators(object):
    welcome_link_id = (By.ID, 'welcome')
    logout_button_link_text = (By.LINK_TEXT, 'Logout')
    admin_button_id = (By.ID, 'menu_admin_viewAdminModule')
    job_sub_btn_admin_id = (By.ID, 'menu_admin_Job')
    menu_job_title_button_id = (By.ID, 'menu_admin_viewJobTitleList')


class JobTitlePageLocators(object):
    add_button_id = (By.ID, 'btnAdd')
    job_title_textbox_id = (By.ID, 'jobTitle_jobTitle')
    job_description_textbox_id = (By.ID, 'jobTitle_jobDescription')
    save_job_button_id = (By.ID, 'btnSave')
    title_results_xpath = (By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[2]')
    delete_button_id = (By.ID, 'btnDelete')
    confirm_delete_button_id = (By.ID, 'dialogDeleteBtn')

    @staticmethod
    def checkbox_result(number):
        xpath = (By.XPATH, '//tbody/tr[' + number + ']//input[@type="checkbox"]')
        return xpath
