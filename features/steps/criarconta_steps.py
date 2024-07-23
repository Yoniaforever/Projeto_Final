from behave import given,when,then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

@given(u'Que o usuario está na pagina de registro')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/register/')
    title = context.browser.title

    assert 'Joga Junto' in title, "Titulo não encontrado"

@when(u'Preencher os dados do formulario')
def step_impl(context):
    cria_email = context.browser.find_element(By.NAME, "email").send_keys(context.email)
    cria_senha = context.browser.find_element(By.NAME, "password").send_keys('AAAAb')
    conf_senha = context.browser.find_element(By.NAME, "confirmPassword").send_keys('AAAAb')


@when(u'apertar em enviar')
def step_impl(context):
    enviar = context.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/button').click()

@then(u'Abre pagina de login')
def step_impl(context):
    title = context.browser.title

    assert 'Joga Junto' in title, "Titulo não encontrado"