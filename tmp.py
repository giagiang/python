# str = "You are an awesome man"
# def tinh_tong(a, b=5 ):
#     return a+b
    

# print(tinh_tong('a','b'))                
# print(tinh_tong(1, 4))                
# duyet tung phan tu:
# for word in original_list:
#     print(word)

# kiem tra do dai
# len("aaa") > 3

# str = "CodeLearn helps you reach your goal"
# chuoi = str.split(" ")
# value = [] 
# for do_dai in (chuoi):
#     if len(do_dai)>4:
#         value.append(do_dai)
# print(value)        


str ="You are an awesome man"
chuoi = str.split(" ")
value = []
def do_dai (str):
    if len(str)>3:
        return True
for word in chuoi :
    if do_dai(word):
        value.append(word)
print(value)                 
