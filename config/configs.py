import time


class TestData:
    # Chrome_executable_path = '/Users/amit.saxena/Downloads/chromedriver'
    # Firefox_executable_path = ''

    base_url = 'https://www.papertrail.com/'
    user_name = 'saxenaamit9225@gmail.com'
    password = 'Tue@25tue'
    login_page_title = "Papertrail - cloud-hosted log management, live in seconds"
    new_name = "Test User" + str(time.time())
    profile = 'https://papertrailapp.com/account/profile/'
