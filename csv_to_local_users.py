import pandas as pd
import numpy as np
import string
import random
from unidecode import unidecode
import subprocess as sub


def password_generator(tam=10):
    password = ""
    chars = [string.ascii_letters, string.punctuation, string.digits]
    for i in range(tam):
        charTypeValue = np.random.choice([0, 1, 2], p=[0.8, 0.1, 0.1])
        charType = chars[charTypeValue]
        password += random.choice(charType)
    return password


def user_generator(string):
    return unidecode(string.lower().replace(' ', ''), 'uft-8')


dados = pd.read_csv('user_emails.csv', sep=';', header=None)

# Bloco command:
# 1) Adiciona o usuário da criado à variável newuser do Powershell
# 2) Adiciona a senha da criado à variável newpassword do Powershell
# 3) Cria um usuário local com o nome: newuser e senha:newpassword
# 4) Adiciona esse usuáro ao Grupo correto do Windows

for person in dados.iloc[:, 0]:
    user = user_generator(person)  # Cria um usário a partir do nome e sobrenome
    password = password_generator()  # Cria uma senha aleatória de 10 digítos
    command = """
    $newuser = """ + f'"{user}"' """
    $newpassword = ConvertTo-SecureString """ + f'"{password}"' + """ -AsPlainText -Force
    New-LocalUser -Name $newuser -Password $newpassword
    Add-LocalGroupMember -Group "Administrators" -Member $newuser
    """
    print(command)
    exec = sub.Popen(["powershell", "& {" + command + "}"])