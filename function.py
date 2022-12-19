'''exercise 87'''

# def delivery(count):
#     return 10.95 + (count - 1) * 2.95

# print(delivery(4))

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
#     lenght = random.randint(7 , 11)
#     password = ''
#     for i in range(lenght):
#         password += chr(random.randint(33,126))
#     print(password)

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

'''exercise'''

        