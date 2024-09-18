import datetime import datetime

data_nascimento = input('informe sua data de nascimento (dd/mm/aaaa): ')

data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_atual = datetime.now()

idade = data_atual.year - data_nascimento.year

print(f'Você tem {idade} anos de idade')