# res = [1,2,3,4,5,6,7,8,9]
# lengths = 1
# for i in range (lengths):
#     res.append(0)
# sochan = []
# for v in res:
#     if v % 2 == 0:
#         sochan.append(v)
# print(sochan)        



# res = [1,2,3]
# lengths = 2
# for i in range (lengths):
#     n = 1
#     res.append(n)
# def evenNum(res):
#     sochan = []
#     for v in res:
#         if v % 2 == 0 :
#             sochan += [v] 
#     return sochan
# print (evenNum(res))    


# a= 3 
# b = 4 
# def power(a,b):
#     return pow(a,b)
# print(pow(a,b))            

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# # đệ quy 
# print(factorial(2))
 


# a = 12 
# b = 14
# def gcd(a,b):
#     if b == 0 :
#         return a ;   
#     return gcd(b,a%b);
# print ("Ước số chung lớn nhất của ",a,"và",b, "la:",gcd(a,b))        
    
# a = 33
# b = 20
# c = 15

# if a == b and b == c:
#     print ('tamgiacdeu')
# elif a==b or b == c or c == a:
#     print('tamgiaccan')  
# else:
#     print('tamgiacthuong')     

# #Initial list
# res = []

# # Input lengths
# lengths = int(input("input so luong:"))

# # Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input("input so:"))
#     res.append(n)




# lengths = int(input("input so luong:"))
# print(type(lengths))

# lengths = int(input("input so luong:"))
# print(type(lengths))


# str = ""
# for element in res:
#     print(f"el {element} {type(element)}")








# so = int(input("please input:"))


# print("truoc khi cast:", so)
# print("truoc khi cast type(so)", type(so))
# so = str(so)
# print("sau khi cast:", so)
# print("sau khi cast type(so)", type(so))

# res = [3,4,5]
# length = 1
# for i in range(length):
#     n = 0
#     res.append(n)
# a = str()
# for i in res:
#     print(res)
#     a=a+str(i)
# print(a)




# #Initial list
# res = []

# # Input lengths
# lengths = int(input())

# Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input())
#     res.append(n)
# chuoi = ''
# res = []
# for so in res:
#     chu = str(so)
#     chuoi = chuoi + chu
#     res.append(word)
# print(chuoi)    
     


# chuoi = str()
# for i in res :
#     chuoi = chuoi + str(i)
# print(chuoi)    

     


# s = "giing"
# def format(s):
#     if len(s)>3:
#         if s.endswith("ing"):
#             print(s+'ly')
#         else:
#              print(s+'ing')
#     else:
#         print(s)
# format(s)        

# s = "giang"
# b= "ly"
# c="ing"
# def format(s):
#     if len(s)<3:
#         a=s
#     else:
#         if s[len(s)-3:] =="ing":
#             a=s+ b
#         else:
#             a=s+ c
#     return a


# print(format(s))


# res = [3,4,5]

# length = 1

# for i in range(length):
#     n = 0
#     res.append(n)
# chuoi = ""
# for i in res :
#     chuoi = chuoi + str(i)
# print(chuoi)       

# n = 12 
# def sum_of_all(n):
#     tong = []
#     for i in range (1,n):
#         if n % i == 0 :
#             tong.append(i)
#             a = sum(tong)
#     return a
# print(sum_of_all(n))                

# n = 66
# def is_abundant(n):
#     sum_value = 0
#     for i in range (1,n+1):
#         if n % i == 0 :
#             sum_value += i 
#         if sum_value > n:
#             return True 
#         else:
#             return False
# print(is_abundant(n))            



# n= 66 
# def is_abundant(n):
#     sum_value = []
#     for i in range (1,n):
#         if n % i == 0 :
#             sum_value.append(i)
#             m = sum(sum_value)
#         if m > n :
#             t = 'True'
#         else:
#             t ='False' 
#     return t        
# print(is_abundant(n))                

n = 55 
def is_abundant(n):
    value = [] 
    for i in range (1,n):
        if n % i == 0 :
            value.append(i)
            m = sum(value)
        if m > n:
            t = 'True'
        else :
            t ='False'
    return t
print(is_abundant(n))       
                                              

 



