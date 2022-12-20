'''exercise 87'''

# def delivery(count):

#     return 10.95 + (count - 1) * 2.95

# print(delivery(4))

'''exercise 91'''

# def func():
    
#     year = int(input('Year'))
#     day  = int(input('Day'))
#     months = int(input('Month'))
#     sum_ = 0
#     day_ = [31,29,31,30,31,30,31,31,30,31,30,31]
#     for i in range(months -1):
#             sum_ += day_[i]
#     sum_ = sum_ + day
#     print(sum_)
         
# func()

'''exercise 92'''

# def func():
    
#     year = int(input('Year'))
#     day  = int(input('Day'))
#     months = 0
#     if year % 4 == 0: 
#         day_ = [31,29,31,30,31,30,31,31,30,31,30,31]
#         for i in day_:
#             months += 1
#             if i > day :
#                 break
#             else:
#                 day = day - i 
#         print(day,months,year)

# func()

'''exercise 93'''

# def func(one,two,three):

#     if one > two + three:
#         return(False)
#     elif two > one + three:
#         return(False)
#     elif three > two + one:
#         return(False)
#     else:
#         return(True)

# one = int(input('enter one '))
# two = int(input('enter two '))
# three = int(input('enter three '))

# print(func(one,two,three))


'''exercise 98'''

# def func(n):

#     for i in  range(2,n // 2+1):
#         if n % i == 0:
#             return 'complex number'
#     else:
#         return'prime number'

# def main() -> None:
#     print(func(n))
# if __name__ == '__main__':
#     n = int(input('enter number: '))
#     main()

'''exercise 99'''

# def func(n):
    
#     while True:
#         n += 1
#         for i in  range(2,n // 2+1):
#             if n % i == 0:
#                 break
#         else:
#             return n 
# print(func(int(input('enter number '))))


'''exercise 100'''

# def passwordGen():
    
#     import random
#     length = random.randint(7 , 11)
#     password = ''
#     for i in range(length):
#         password += chr(random.randint(33,126))
#     return password

# passwordGen()

'''exercise 101'''

# import random

# def func():

#     tver = ('1','2','3','4','5','6','7','8','9')
#     tarer = ('Ա','Բ','Գ','Դ','Ե','Զ','Լ','Ի','Պ','Ռ','Ս') 
#     tarer_ = ''
#     tver_ = ''
#     for i in range(3):
#         tver_ += random.choice(tver)
#     for i in range(3):
#         tarer_ += random.choice(tarer)
#     print(tarer_,tver_)
#     tarer_ += random.choice(tarer)
#     print(tarer_,tver_)

# print(func())

'''exercise 102'''

# def password(a):

#     num_count = 0
#     upp_count = 0
#     lower_count = 0

#     for i in a:
#         if i.isnumeric():
#             num_count += 1
#         elif i.isupper():
#             upp_count += 1
#         elif i.islower():
#             lower_count += 1
#     if len(a) >= 8 and num_count > 0 and upp_count > 0 and lower_count > 0:
#         return True
#     else:
#         return False

# print(password(input('Enter your password ')))

'''exercise 103'''

# count = 1
# pass_ = passwordGen()

# while password(pass_) == False: 
#     pass_ = passwordGen()
#     count += 1

# print(count, pass_)








