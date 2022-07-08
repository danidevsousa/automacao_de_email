import win32com.client as win32


#criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email

email = outlook.CreateItem(0)


#configurar as informaçções do seu e-mail
email.To = 'alexandre.roberto9@hotmail.com'
email.Subject = 'E-mail automatico do Python'
email.HTMLBody = """
<p>Olá, bem vindo ao meu primeiro e-mail enviado por código.</p>
"""
anexo = "C://Users/BCR/URI/teste.xlsx"
email.Attachments.Add(anexo)
email.Send()
print("Email enviado")

