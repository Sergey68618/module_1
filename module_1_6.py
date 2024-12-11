# Словари и множества

my_dict = {'Sergey':1981, 'Denis':1986, 'Roman':1991, 'Oleg':1988, 'Leonid':1980}
print("Dictionary:", my_dict)
print("Existing value:", my_dict['Oleg'])
print("Not existing value:", my_dict.get('Masha'))
my_dict.update({'Misha':1982, 'Max':1981})
a = my_dict.pop('Leonid')
print("Deleted value:", a)
print("Modified dictionary:", my_dict)
print()
my_set = {1 , 5 , 1 , 5 , 'Зяблик', 0}
print("Set:", my_set)
my_set.add(3.14)
list = (7, 7, 7)
my_set.add(list)
my_set.discard(0)
print("Modified set:", my_set)