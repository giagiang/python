# s = "abc"
# print(len(s))
# # hàm trả về độ dài chuỗi 

# s = "CODELEARN123"
# print= (s.lower())
# trả về một chuỗi dạng chữ thường 

# s = "codelearn2022"
# print (s.upper())
# chuyển chuỗi thành in hoa 

# s = "codelearn2020"
# print(s.isalnum())
# s = "codelearn2020.io"
# #  Kết quả sẽ là False do chuỗi s chứa ký tự .
# print(s.isalnum())

# s = "codelearn"
# print(s.isalpha())
# # Kết quả sẽ là False do chuỗi s chứa số 2020
# s = "codelearn2020"
# print(s.isalpha())

# s = "2020"
# print(s.isnumeric())
# s = "c2020"
# print(s.isnumeric())

# s = "Welcome to Codelearn.io!"
# print(s.split(" "))
# s = "A1B1C1D1E1"
# print(s.split("1"))
# Phương thức này được dùng để cắt một chuỗi ra thành list các chuỗi khác dựa trên một phần tử trong chuỗi đầu vào:

# lst = ["Welcome", "to", "Codelearn.io!"]
# print(" ".join(lst))
# lst = ["A", "B", "C"]
# print("-".join(lst))
# nối các tập hợp thành một chuỗi kí tự như trước 

# name = "Cod3l3arn"
# print(name.replace("3", "e"))


# s = "giangmadridista"
# print (s.upper())


# s = "ricciardo.io"
# if len(s)<2:
#     print("")
# else:
#     print(s[0:2]+ s[-3:]) 


# s1 = "sum"
# s2 = "moon"
# tmp = s1[0:2] + s2[2:]
# s1 = s2[0:2] + s1[2:]
# s2 = tmp
# print (s1 + " " + s2)

# x = "python"
# print(x[1])

# c = "python"
# print ("a" in c)


# s1 = "sum"
# s2 = "moon"
# tmp = s1[0:2]+ s2[2:]
# s1 = s2[0:2] + s1 [2:] 
# s2 = tmp 
# print(s1 + " " + s2)


# s= "Python Exercies"
# chuoi = s.split(' ')
# # print(chuoi)
# daonguoc =' '.join(reversed(chuoi))

# print(daonguoc)














s = "le gia giang"
chuoi =s.split(' ') 
# print(chuoi)
daonguoc=' '.join(reversed(chuoi))
print(daonguoc)