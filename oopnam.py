# class sieunhan:
#     suc_manh = 50 
#     def __init__(self, para_ten , para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#     def __repr__(self):
#         return 'ten:{}\nvu khi: {}\nmausac: {}'.format(self.ten, self.vu_khi, self.mau_sac)
#     # def __str__(self):
#     #     return 'day la {} , su dung {}'.format(self.ten,self.vu_khi)    
# giaginag_fz =sieunhan('sieu nhan do', 'katana', 'yellow')
# print(giaginag_fz)



# ví dụ về class and ọbject:
# class Car :
#     # thuộc tính lớp
#     loaixe = "ô tô "
#     # thuộc tính đối tượng 
#     def __init__ (self , tenxe  , mausac , nguyenlieu):
#         self.tenxe = tenxe
#         self.mausac = mausac
#         self.nguyenlieu = nguyenlieu
# # instantiate the car class
# lamboghini = Car ("urus","yellow","xang")
# porsche = Car("911","red","dien")
# ferarri = Car("488","orange","xang")
# # access the class attributes
# print("Porscher la {}.".format(porsche.__class__.loaixe))
# print("Lamboghini la {}.".format(lamboghini.__class__.loaixe))
# print("Ferarri la {}.".format(ferarri.__class__.loaixe))

# # access the instance attributes
# print("xe{}co mau{}.{} là nguyên liệu vận hành.".format(porsche.tenxe,porsche.mausac,porsche.nguyenlieu))
# print("xe{}co mau {}.{} la nguyen lieu van hanh.".format(lamboghini.tenxe,lamboghini.mausac,lamboghini.nguyenlieu))
# print("xe{}co mau {}.{}la nguyen lieu van hanh .".format(ferarri.tenxe,ferarri.mausac,ferarri.nguyenlieu))



# phương thức
# class và method
# class Car : 
#     # thuộc tính đối tượng 
#     def __init__(self , tenxe , color, nguyenlieu):
#         self.tenxe = tenxe
#         self.color = color
#         self.nguyenlieu = nguyenlieu

      #phương thức 
#     def dungxe(self , mucdich):
#         return"{} đang dừng xe để {}".format(self.tenxe,mucdich)

#     def chayxe(self):
#         return"{} đang chạy trên đường ". format(self.tenxe)

#     def nomay (self):
#         return"{} đang nổ máy".format(self.tenxe)

# # instantiate the Car class
# toyota = Car("Toyota", "Đỏ", "Điện")
# lamborghini = Car("Lamborghini", "Vàng", "Deisel")
# porsche = Car("Porsche", "Xanh", "Gas")

# # call our instance methods
# print(toyota.dungxe("nạp điện"))
# print(lamborghini.chayxe())
# print(porsche.nomay())



# kế thừa (Inheritance)

# class Car:
#     # Constructor
#     def __init__(self, hangxe , tenxe, mauxe):
#     # lớp car có 2 thuộc tính : tenxe , màu xe , hãng xe 
#         self.hangxe = hangxe
#         self.tenxe = tenxe 
#         self.mauxe = mauxe

#         #phuong thuc
#     def chayxe(self):
#          print("{}đang chay trên đường".format(self.tenxe)) 

#     def dungxe(self,mucdich):
#         print("{} đang chay trên đương {}".format(self.tenxe,mucdich))

#         #lớp HONDA mở rộng từ lớp car :
# class  Honda(Car):
#     def __init__(self,hangxe, tenxe,mauxe,nguyenlieu):
#           # Gọi tới constructor của lớp cha (Car) 
#         # để gán giá trị vào thuộc tính của lớp cha.
#         super().__init__(hangxe,tenxe,mauxe)

#         self.nguyenlieu = nguyenlieu
#      # Kế thừa phương thức cũ
#     def chayxe(self):
#         print("{} đang chay xe trên đường".format(self.tenxe))

#      # Ghi đè (override) phương thức cùng tên của lớp cha.
#     def dungxe(self, mucdich):
#         print("{}đang dung xe de{}".format(self.tenxe,mucdich))
#         print("{}chay bang{}".format(self.tenxe,self.nguyenlieu))

#     #bổ xung thêm thành phần mới 
#     def nomay(self):
#         print("{}đang nổ máy".format(self.tenxe))

# honda1 = Honda("honda","hondaxe","do","xang")
# honda2 = Honda("honda","honđakkk","vang","dien")
# honda3 = Honda("honda","hondadream", "trang", "gas")

# honda1.dungxe("nap điện")
# honda2.chayxe()
# honda3.nomay()



# đóng gói (encapsulation)

class Computer:

     def __init__(self):
        # Thuộc tính private ngăn chặn sửa đổi trực tiếp
        self.__maxprice = 900

     def sell(self): 
        print("Giá bán sản phẩm: {}".format(self.__maxprice))

     def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# thay đổi giá.
c.__maxprice = 1000
c.sell()

# sử dụng hàm setter để thay đổi giá.
c.setMaxPrice(1000)
c.sell()





# Đa hình(polymorphism)
# class Toyota:

#      def dungxe(self):
#         print("Toyota dừng xe để nạp điện")

#      def nomay(self):
#         print("Toyota nổ máy bằng hộp số tự động")

# class Porsche:

#      def dungxe(self):
#         print("Porsche dừng xe để bơm xăng")

#      def nomay(self):
#         print("Porsche nổ máy bằng hộp số cơ")

# # common interface
# def kiemtra_dungxe(car): car.dungxe()

# # instantiate objects
# toyota = Toyota()
# porsche = Porsche()

# # passing the object
# kiemtra_dungxe(toyota)
# kiemtra_dungxe(porsche)


# hàm len
# a = 'giagiang'
# print(len(a))
# print(a.__len__())

# def __len__(self):
#     return len(self.ten)



# toán tử cộng  
# print(2+3)
# print(int.__add__(2,3))
# print('giagiang'+' never give up')
# print('ronaldo'+' Super proud of you')
# print(str.__add__('how','kteam'))
# print([1,2]+[8,9])
# print(list.__add__([1,2],[3,4]))


# def __add__(self , gia_giang_prasdfas_dasdas_asd_):
#     return self.suc_manh + gia_giang_prasdfas_dasdas_asd_.suc_manh
# print()    




