# def giang():
#     for i in range (1,22):
#         print(i ,end="")
#         # end ="" có nghiã là sử dụng hàm prin và không xuống dòng 
#     print()
# giang()
# giang()        


# def neu_la_a(lst):
#     answer = 0 
#     for v in lst:
#         answer += v 
#     return answer
# print(neu_la_a([3,4,5]))
# print(neu_la_a([4,5,6]))
# print(neu_la_a([1,2,3]))       


# def count_event(lst):
#     count = 0 
#     for i in lst:
#         if i % 2 == 0:
#             count +=1
#     return count
# print(count_event([7,2,4]))             

# def tong (lst):
#     answer = 0 
#     for i in lst :
#         answer += i
#     return answer
# lst = [2,1,6]
# n = 3
# for v in range(n):
#     lst.append(4)
# print(lst)    
# print(tong(lst))  

# def big(a,b,c):
#     if a>b and a> c:
#         return a
#     return b if b > c else c
# a = 8 
# b = 7 
# c = 5
# print(big(a,b,c))         
            
# def sum(a, b):
#     print("sum = " + str(a + b))
# sum('a','b')


# def show(s):
#     upper = 0 
#     lower = 0 
#     for c in s:
#         if c.isupper():
#             upper += 1
#         if c.islower():
#             lower +=1
#     print("Given String:",s)
#     print("Number of uppercase letters:",upper)
#     print("Number of lowercase letters:",lower)
# s ="You Are Apple In My Eye"
# show(s)     
       




# def nhan_gia_tri(lst):
#     answer = []
#     for i in lst :
#         if i not in answer:
#             answer.append(i)
#     return answer
# n = 1 
# lst = [2,2,2,3,3,1]
# for v in range (n):
#     lst.append(4)
# print(nhan_gia_tri(lst))            

# def tong(a,b):
#     print('a',a)
#     print('b',b)
# tong(a=3,b = 4)
 

# def giang(c,d):
#     print('c',c)
#     print('d',d)
# giang(c= 11,d = 100)

# def teo(a,b= 2,c = 3 ,d= 4):
#     f=(a+d)*(b+c)
#     print(f)
# teo(1,2,3,5)     


# def big(a,b,c):
#     if a> b and a> c:
#         return a 
#     return b if b >c else c
# a = 3 
# b = 6 
# c = 5 
# print (big(a,b,c))   

# def show(lst):
#     answer=0 
#     for i in lst:
#         answer += i
#     return answer
# lst = [1,2,5]
# n = 3 
# for v in range (n):
#     lst.append(0)
# print(show(lst))            

# def max(a,b,c):
#     if a>b and a > c :
#         return a 
#     return b if b > c else c 
# a = 9 
# b = 10 
# c = 11
# print(max(a,b,c))  


# def show(lst):
#     inhoa = 0 
#     inthuong = 0 
#     for c in lst:
#         if c.isupper():
#             inhoa += 1 
#         if c.islower():
#             inthuong += 1 
#     print("Given string:",lst)
#     print("number of uppercase letters:",inhoa)
#     print("number of lowercáe letters:", inthuong)      
# lst = "Given string: You Are Apple In My Eye"
# show(lst)       

# def kteam(greating, name='giagiang'):
#     print(greating,name + '!')

# kteam('hello')


# def f(kteam=[]):
#     kteam.append('F')
#     print(kteam)
# f()       
# f()
# f([1,2,3])

# def kteam(a,b):
#     print(a,b)
# kteam(a=3,b='free education')

# def value(a,b):
#     print('a',a)
#     print('b',b)
# value(a=3,b=4)
# value(b=3,a=4)  

# def teo_wiht_some(name,varb):
#     print('teo',varb +'s',name)
# teo_wiht_some('python','anny')
# teo_wiht_some('html',varb='like')
# # teo_wiht_some('css',name='gianng')


# def teo(a, b=2, c= 3, d= 4):
#     f= (a+d)*(b+c)
#     print (f)
#     print(a)
# teo(1,2,3,7)  

# def value(giang,key,*,key_2):
#     print(giang)
#     print(key)
#     print(key_2)
# #  dấu * dùng để thay thế luôn từ khoá trước 
# value(1,2,key_2='beo')


# def kteam(k,t,e,r):
#     print(k)
#     print(t,e)
#     print('end',r)
# lst=['1234','giang', 99.99,'ronaldo']
# kteam (*lst)



# def x (k,t,c,*,e='beo'):
#     print(k)
#     print(t,c)
#     print ('end',e)
# lst= ('123','giang',99.22)
# x (*lst,e='kter')    

# def a (*,s,d):
#     print(s,d)
# a(*('a','b'))


# def moto(*args,kter):
#     print(args)
#     print(kter)
#     print(type(args))
# moto('kteam',69.60,kter='henrry')
# moto(*(x for x in range(7)),kter = 'aloloa')
   

# def kteam(name,member):
#     print('name=>',name)
#     print('member=>',member)
# dic = {'name':'giang', 'member':99}
# kteam(**dic)        
    


# def kteam(**kwwargs):
#     print(kwwargs)
#     print(type(kwwargs))
# kteam(name='kteam', member = 99)


# def giang(**answer):
#     for key, value in answer.items():
#         print(key,'=>',value)
# giang(id = 100, name='cuti', tuoi= 55, lang='pyhton')



# def felix(*args,** kwargs):
#     print(args)
#     print(kwargs)
# felix (name ='giang', age = '19')
# felix (*(x for x in range(7)),args= 100)
    


# def sum_of_list(lst):
#     answer = 0
#     for v in lst:
#         answer += v
#     return answer

# lst = [1,2,3]
# answer = 0
# for v in lst:
#     answer += v


# lst = [4,5,6]
# answer = 0
# for v in lst:
#     answer += v

# sum_of_list([1,2,3])
# sum_of_list([1,6,3])


# def hhhjbnjhbjhbjhb():
#     # answer = []
#     # for v in lst:
#     #     if v not in answer:
#     #         answer.append(v)
#     # return answer
#     return [1,2,4]

# n = 1
# lst = [2, 2, 2, 3, 3, 1, 0]
# for i in range(n):
#     lst.append(0)

# ans =  hhhjbnjhbjhbjhb()   
# # ans =  [1,2,4]   
# print(ans)

# def get_unique_values(lst):
#     answer = []
#     for i in lst :
#         if i not in answer:
#             answer.append(i)
#     return answer
# a = 1
# lst = [2,2,3,3,3,4,4,1]
# for i in range (a):
#     lst.append(0)
# print(get_unique_values(lst))  

# def sotunhien(n):
#     count = 0 
#     for i in range (1,n+1):
#         if n % i == 0:
#             count += 1
#     if count == 2 :
#         return True
#     return False             

# n = 9 
# print(sotunhien(n))

# str = "You are an awesome man"
# chuoi=str.split(" ")
# value = []

# def check_length(str):
#     if len(str)>3:
#         return True
#     # else:
#     #     return False    

# for word in chuoi:
#     if check_length(word):
#         value.append(word)
# print(value)        
              

# res = [3,4,5]
# length = 1
# for i in range (length):
#     n = 0 
#     res.append(n)
# chuoi=" "
# for i in res :
#     chuoi=chuoi+ str(i)
# print(chuoi)  



s = "abcing"
def format(s):
    if len(s)>3:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing' 
        return s 
    else:
        return s 
print(format(s))                  