#Getter  là lấy ra 


# class kter:
#     def __init__(self, ho , ten ):
#         self.ho = ho 
#         self.ten = ten 
#         # self.email = ho + '-' + ten + '@cuchuoi.com'
#     @property    
#     def ho_va_ten (self):
#         return '{} {}'.format(self.ho , self.ten)
#     @property    
#     def email(self):
#         return self.ho + '-' + self.ten + '@cuchuoi.com'    
# kter_A = kter ("tran" , "giang ricciardo")

# kter_A.ho = "nguyen"
# kter_A.ten = "giang"

# print(kter_A.ho)
# print(kter_A.ten) 
# print(kter_A.email)
# print(kter_A.ho_va_ten)          


 
#setters là cài vào 

# class Car : 
#     def __init__(self , hang_xe , ten_xe):
#         self.hang = hang_xe
#         self.ten = ten_xe
#     @property
#     def email(self):
#         return self.hang + '-' + self.ten + '@ferarri.com'
#     @property
#     def ten_hang_xe(self):
#         return '{} {}'.format(self.hang, self.ten)
#     @ten_hang_xe.setter
#     def ten_hang_xe(self, ten_moi):
#         hang_moi,ten_moi = ten_moi.split(' ')
#         self.hang = hang_moi
#         self.ten = ten_moi

# Car_fz = Car("ferarri","highbercar")

# Car_fz.ten_hang_xe= "Toyota xe"

# print(Car_fz.ten_hang_xe)


        
# #deleter 
class Kter:
    def __init__(self, ho , ten):
        self.ho = ho 
        self.ten = ten 
    @property
    def email(self):
        return self.ho + '_' + self.ten + '@kteam.com'
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho ,self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('Da Xoa')

kter_A = Kter("Tran", "Long")

kter_A.ho_va_ten = "gia giang"

print(kter_A.ho_va_ten)


del kter_A. ho_va_ten

print(kter_A.ho)
print(kter_A.ten)
