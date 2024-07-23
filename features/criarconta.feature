# language: pt

Funcionalidade: formulario de criação de contas
    Cenario: criando um conta no Backoffice

    Dado Que o usuario está na pagina de registro
    Quando Preencher os dados do formulario
    E apertar em enviar
    Então Abre pagina de login
