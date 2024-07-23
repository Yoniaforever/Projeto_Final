from selenium.webdriver import Firefox
from faker import Faker

def before_all(context):
     context.browser = Firefox()
     context.fake = Faker('pt_BR')
     context.email = context.fake.free_email()
    
def After_all(context):
    context.browser.quit()