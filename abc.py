# a = int(input("No.1: "))
# b = int(input("No.2: "))
# c = int(input("No.3: "))

# if a <= b:
#     if b <= c:
#         print(c)
#     else:
#         print(b)
# else:
#     if a >= c:
#         print(a)
#     else:
#         print(c)


# a = 10
# b = 11 
# c = 12 

# if a <= b :
#     if b <= c :
#         print(c)
#     else:
#         print(b) 
# else:
#     if a >= c: 
#         print(a)     
#     else:
#         print(c)                       


# a = 3 
# while a > 0:
#     print('a=', a )
#     a -= 1 

cho_nam_so = []
g_so = 1 
while True:
    if  g_so % 2 == 0 :
        cho_nam_so.append(g_so)
        if len(cho_nam_so) >= 5 :
            break
    g_so += 1 
print(cho_nam_so)
print(g_so)        
    