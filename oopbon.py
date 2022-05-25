# class SieuNhan :
#     pro = 123 

# class SieuNhanPro(SieuNhan):
#     pass 

# gao_do = SieuNhanPro()
# print(gao_do.pro)

# class sieunhan:
#     suc_manh = 99 

# class sieunhangao(sieunhan):
#     suc_manh = 30 
# giagiang = sieunhangao()
# print(giagiang.suc_manh)

# kế thừa hàm constructor


# class sieunhan:
#     suc_manh = 99 
#     def __init__(self,para_ten , para_vu_khi, para_mau_sac):
#         self.ten=para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac

# class sieunhangao(sieunhan):
#     suc_manh = 89
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac,para_bien_hinh):
#         # self.ten=para_ten
#         # self.vu_khi=para_vu_khi
#         # self.mau_sac=para_mau_sac
#         super().__init__(para_ten,para_vu_khi,para_mau_sac)
#         self.bien_hinh=para_bien_hinh


# giagiang_fz = sieunhangao("gao do","kiem","do","backgoku")
# print(giagiang_fz.__dict__)
# print(giagiang_fz.suc_manh)        
# fz_dict = giagiang_fz.__dict__
# ten = fz_dict.get("ten", "khong co ten")
# ten = fz_dict["ten"]  
# ten = giagiang_fz.ten  # attribute


# kế thưa phuơng thức
# class mau_giao :
#     si_so = 59 
#     def __init__(self, para_ten , para_do_dung, para_mau_sac):
#         self.ten= para_ten
#         self.do_dung=para_do_dung
#         self.mau_sac = para_mau_sac
#     def hello(self):
#         print("xin chao,ta la", self.ten)
#     def show_su_manh(self):
#         print("si so cua ta la ",self.si_so)

# class mau_giao_be(mau_giao):
#     si_so = 49 
#     def __init__(self , para_ten,para_do_dung, para_mau_sac,para_su_thu):
#         super().__init__(para_ten, para_do_dung, para_mau_sac)
#         self.su_thu= para_su_thu
#     def show_si_so(self):
#         print("si so cua ta la", self.si_so)
#         print("su dung thu do ", self.su_thu)
# giagiang_fz = mau_giao("sieu nhan","sach","yeallow")
# giagiang_po = mau_giao_be("ca tram","but", "yellow","su tu ")

# giagiang_fz.hello()
# giagiang_po.hello()

# giagiang_fz.show_su_manh()
# giagiang_po.show_su_manh()

