'''exercise 152'''

# x = open(input('enter file name '),'a')
# y = open('exercise152.py')
# r = y.readlines()
# count = 1
# for i in r:
#     x.write(str(count) + ') '+i)
#     count += 1

'''exercise 153'''

# x = open('exercise152.py','r')
# y = x.read()
# j = y.split(' ')
# list_ = []
# for i in j:
#     list_.append(len(i))
# for i in j:
#     if len(i) == sorted(list_)[-1]:
#         print(f'{sorted(list_)[-1]} {i} ')

'''exercise 154'''

# x = open('exercise152.py', 'r')
# y = x.read()
# b = {}
# for i in y:
#     if i.isalpha():
#         b[i]=y.count(i)
# print(b)

'''exercise 155'''

# x = open('exercise152.py', 'r')
# y = x.read()
# o = ',./!@#$%^&*()_+":;'
# for i in y:
#     if i in o:
#         y = y.replace(i,'')
# j = y.split(' ')
# b = {}
# for i in j:
#     b[i] = j.count(i)
# for i in b:
#     print(i,b[i])

'''exercise 156'''

# count = 0 
# while True:
#     x = input('enter ')
#     if x == '':
#         break
#     try:
#         count += float(x)
#     except ValueError:
#         print('enter number')
# print(count)

'''exercise 157'''

# x = input('enter ')
# try:
#     if int(x) == 1:
#         print('a')
#     elif int(x) == 2:
#         print('b')
# except ValueError:
#     try:
#         if x == 'a':
#             print('1')
#         elif x == 'b':
#             print('2')
#     except ValueError:
#         print('enter number or letter ')





# class Change:

#     def __init__(self,a):
#         self.a = a
    
#     def dollar(self):
#         return self.a / 390
    
#     def euro(self):
#         return self.a / 400

#     def funt(self):
#         return self.a / 500

# C = Change(int(input('enter dram ')))
# print(f'{round(C.dollar(),2)}''$')


# class Soda:
#     def __init__(self, ingredient):
#         self.ingredient = ingredient

#     def show_my_drink(self):
#         if isinstance(self.ingredient, str):
#             self.ingredient = None
#         elif self.ingredient:
#             return (f'Gazirovka  {self.ingredient}')
#         else:
#             return'Obichnaya Gazirovka'

# d = Soda(input('enter ingredient: '))
# print(d.show_my_drink())
