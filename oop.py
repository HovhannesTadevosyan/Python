# class KgToPounds:

#     __kg = 5
    
#     def to_pounds(self):
#         return self.__kg * 2.2 

#     def set_kg(self,nor_kg):
#         self.__kg = nor_kg
    
#     def get_kg(self):
#         return self.__kg

# Gor = KgToPounds()
# Gor.set_kg(10)
# print(Gor.to_pounds())
# print(KgToPounds._KgToPounds__kg)



# class Nikol:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

#     def payman (self):
#         if self.__name == 'Nikolay':
#             return 'my name is Nikolay'
#         else:
#             return (f'my name is not {self.__name}')
    
# Gor = Nikol(input('name '),input('age '))
# print(Gor.payman())


# class RealString:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def lennn(self):
#         if len(self.a) > len(self.b) :
#             return self.a
#         elif len(self.a) == len(self.b) :
#             return '='
#         else :
#             return self.b

#     def ordd(self):
#         s,m = 0,0
#         for i in self.a:
#             s += ord(i)
#         for j in self.b:
#             m += ord(j)
#         if m > s :
#             return self.b
#         elif m < s :
#             return self.a
#         else:
#             return '='

# Vzgo = RealString(input('aaa'),input())
# print(Vzgo.lennn())

# import random

# class Game:

#     a = 100
#     b = 100

#     def __init__(self,vardan,levon):
#         self.vardan = vardan
#         self.levon = levon

#     def games(self):
#         while True:
#             udar = random.choice(('vardan','levon'))
#             if udar == 'vardan':
#                 self.b -= 20
#             else:
#                 self.a -= 20
#             if self.a == 0:
#                 return 'Win Levon'
#             else:
#                 return 'Win Vardan'
            
# ret = Game('vardan','levon')
# print(ret.games())
    


# class Student:

#     def __init__(self,anun,xumb,baller):
#         self.anun = anun
#         self.xumb = xumb
#         self.baller = baller
    

#     def cank(self):
#         a = []

# class Roditel:

#     def __init__(self,name,age,deti:list):
#         self.name = name
#         self.age = age
#         self.deti = deti

#     def inform(self):
#         return 'Good'

#     def x(self):
#         return 'Nice'

#     def y(self):
#         return 'xxx'

#     def __(self):
#             def name1(self,namedeti):
#                 return 'Mike'
            
#             def age1(self,agedeti):
#                 return '10'
            
            

# aaa = Roditel('vardan',50,['Aram','Grig'])
# print(aaa.)




# class Dar:

#     def __init__(self,taretiv): 
#         self.taretiv = taretiv
    
#     def dar(self):
#         if self.taretiv %100 == 0:
#             return self.taretiv//100
#         else:
#             return self.taretiv//100 + 1

# dar1 = Dar(1800)
# print(dar1.dar())
        




'''PaginationHelper'''

# class PaginationHelper:

#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page

#     def page_count(self):
#         if self.collection % self.items_per_page == 0:
#             return self.collection // self.items_per_page
#         else:
#             return self.collection // self.items_per_page + 1
     
#     def item_count(self):
#         return len(self.collection)

#     def page_item_count(self, item_index):
#         self.item_index = item_index
#         if self.collection // self.item_index:
    
#     def page_index(self, page_index):
#         self.page_index = page_index
#         if self.page_index > len(self.collection) or self.page_index < 0:
#             return -1
#         else:
#             if len(self.collection)% self.page_index == 0:
#                 return self.collection // self.page_index
#             else:
#                 return self.collection // self.items_per_page +1




# def split_the_bill(x):
#     y = list(x.values())
#     d = 0
#     b = {}
#     for i in y:
#         d += i
#     d = d / len(x.values())
#     for i in x.keys():
#         b[i] = round(x[i] - d,2)
#     return b


# ddd = split_the_bill({'A': 20, 'B': 15, 'C': 10})
# print(ddd)



# class Block:

#     def __init__(self,x):
#         self.a = x[0]
#         self.b = x[1]
#         self.c = x[2]

#     def get_width(self):
#         return self.a

#     def get_length(self):
#         return self.b

#     def get_height(self):
#         return self.c

#     def get_volume(self):
#         return self.a * self.b * self.c

#     def get_surface_area(self):
#         return self.a * self.b * 2 + self.a * self.c * 2 + self.b * self.c * 2

# block1 = Block([2,2,2])
# print(block1.get_surface_area())


# class Person:

#     def __init__(self,my_name):
#         self.my_name = my_name

#     def greet(self,your_name):
#         self.your_name = your_name
#         return f"Hello {self.your_name}, my name is {self.my_name}" 

# jack = Person("Jack")
# jill = Person("Jill")
# print(jack.greet('kkk'))

# class Student:

#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties

# def most_money(students):
#     b = {}
#     for i in students:
#         b[i.name] = i.fives *5 + i.tens*10 + i.twenties*20
#     if b.values().count(max(b.values()))>1:
#         return "all"
#     else:
#         max_key = max(b, key =b.get)
#     return max_key


# phil = Student("Phil", 2, 2, 1)
# cam = Student("Cameron", 2, 2, 0)
# geoff = Student("Geoff", 0, 3, 0)

# most_money([cam, geoff, phil])








