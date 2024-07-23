from behave import given,when,then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


@given(u'Que estou na pagina de Login')
def step_impl(context):
   context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
   title = context.browser.title

   assert 'Joga Junto' in title, "Titulo não encontrado"

@when(u'preencho o formulario de login')
def step_impl(context):
    env_email = context.browser.find_element(By.NAME, 'email').send_keys(context.email)
    env_senha = context.browser.find_element(By.NAME, 'password').send_keys('AAAAb')
    
@when(u'aperto em enviar')
def step_impl(context):
    login = context.browser.find_element(By.XPATH, '//*[@id="root"]/main/form/button').click()

@then(u'entro no site')
def step_impl(context):
    title = context.browser.title

    assert 'Joga Junto' in title, "Titulo não encontrado"