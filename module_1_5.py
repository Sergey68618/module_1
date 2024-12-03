# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
Immutable_var = (1, 'string', True, [4, 7])
print('Immutable_var:', Immutable_var)
# Immutable_var[1] = 5  # приводит к ошибке TypeError: 'tuple' object does not support item assignment
# кортеж является неизменяемой упорядоченной коллекцией, однако есть один нюанс...
Immutable_var [3][0] = 10 # можно поменять элементы внутреннего списка кортежа
Mutable_list = [8, "Cat", False]
Mutable_list [1] = "Dog"
Mutable_list.append('Modified')
print('Mutable_list:', Mutable_list)