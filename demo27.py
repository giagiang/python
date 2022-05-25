# # g = range(3)
# # print(type(g)) 

# # k = range(3)
# # print(k[1])

# # lst = [1,2,3]
# # for value in lst:
# #     value += 1 
# # print(lst)    

# lst = [2, 6, 9, 2]
# # # 2, 6 , 9, 2]
# # # [6, 12, 18,  6]
# for item in enumerate(lst):
#     # print(item)
#     index, value = item
#     print(value)
#     # if lst[i] % 3 == 0:    
#     #     lst[i]  = lst[i] * 2  
#     # else:
#     #     lst[i] = lst[i] * 3
#     #     print(i)
#     #     pass

# # print(lst)    

# # # import math 
# # from math import sqrt

# # numbers = [100,49,33,44,55]

# # ne_list = [sqrt(n) for n in numbers]
# # print(ne_list)


# # number_list = [1, 2, 3]
# # str_list = ['one', 'two', 'three']

# # result = zip(number_list, str_list)

# # print(list(result))


# lst_father = [[1,2,3], [4,5,6]]

# for list_child in enumerate(lst_father):
#     print(list_child)
# #     list_child[1][2]= None
# # print(lst_father)        


# for index, value in enumerate(lst_father):
#     # print(list_child)
#     # list_child[1][2]= None
#     # print(index)
#     # print(value)
#     value[0]= None
# print(lst_father)       

# lst = [[1,2,3], [4,5,6]]
# for i in range (len(lst)):
#     print(i)
#     print(lst[i])


# s = "databasesystem"
# for c in s:
#     # print(c)
#     print("current", c)
# print (s)    
    
# print("10 * 1 = ", 10)
# a = 6
# for i in range(5):
#     new_i = i + 1
#     # print(new_i)
    
#     print(f"{a} * {new_i} = {a * new_i}")

# age = 100
# # ange: 80
# # ange: 70
# print("tuoi: {5 * 8}")

# tuoi = 99
# print(f"tuoithat:{tuoi}")
# print(tuoi)

# def format():
#     return ""

# age = 36
# age2 = 37
# txt = "My name is John, and I am {} and {}"
# txt2 = txt.format(age, age2)
# print(txt2)
# print(txt.format(age, age2))


# a = 10 
# for value in range(1,6):
#     print(f"{a} * {value} = {a*value}")

# print(f"{a}* {2} = {a * 2}")    

# a = input("please input:")
# for b in range (5):
#     # c = b + 1
#     print(f"{a} * {b+1} = {a*(b+1)}")


# s = "rainyday"
# for c in s :
#     # print(c)

    # print(c)
    # print("Current character:", c )


# a = int(input("please input a:"))
# b = int(input("please input b:")) 
# count_even = 0 
# count_odd = 0 
# for c in range (a,b+1):
    # print(c)
#     if c % 2 == 0 :
#         count_even += 1 
#     else:
#         count_odd += 1 
# print("tatal even: ",count_even) 
# print(count_odd)           





# s = "databasesystem"
# for c in s :
#     if c != "y":
#         print(f"Current character:{c}")        


# a = 1 
# b = 10 
# sochan = 0 
# sole = 0 
# for tong in range (a , b +1 ):
#     if tong % 2 == 0 :
#         sochan += 1
#     else:
#         sole +=1
# print("tong cac cho chan la :",sochan) 
# print("tong cac so le là :",sole)       \

# n = 10
# b = 0 
# for i in range (1, n+1):
#     b  =  b + i/(i+1)
#     # print(i)
#     # print(b)
# print(round(b,2))

# n = 5 
# a = 0
# for i in range (1,n+1):
#     a += i
# print(a)    

# a = 3 
# b = 9 
# tong = 0 
# for i in range (a,b+1):
#     if i % 2 != 0:
#         tong += i
# print(tong)      

# a = 10 
# for i in range (1,6):
#     print(a,"*",i,"=",a* i)        

n = 10 
b = 0 
for i in range (1 , n+1):  
    b += i / (i+1)
    print(b)
print(round(b,2 ))    