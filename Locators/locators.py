class Locators:

    # Login page objects
    username_textbox_id = 'txtUsername'
    password_textbox_id = 'txtPassword'
    login_button_id = 'btnLogin'
    invalidUsername_message_id = 'spanMessage'

    # Home page objects
    welcome_link_id = 'welcome'
    logout_button_link_text = 'Logout'
    admin_button_id = 'menu_admin_viewAdminModule'
    job_sub_btn_admin_id = 'menu_admin_Job'
    menu_job_title_button_id = 'menu_admin_viewJobTitleList'

    # Job Titles page objects
    add_button_id = 'btnAdd'
    job_title_textbox_id = 'jobTitle_jobTitle'
    job_description_textbox_id = 'jobTitle_jobDescription'
    save_job_button_id = 'btnSave'
    tittle_results_xpath = '//*[@id="resultTable"]/tbody/tr/td[2]'
    delete_button_id = 'btnDelete'
    confirm_delete_button_id = 'dialogDeleteBtn'

    @staticmethod
    def checkbox_result(number):
        return '//tbody/tr[' + number + ']//input[@type="checkbox"]'
