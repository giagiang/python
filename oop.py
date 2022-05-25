# class SieuNhan:
#     pass 
# sieu_nhan_A = SieuNhan()

# sieu_nhan_A.ten ="sieu nhan do"
# sieu_nhan_A.vu_khi = "dao" 
# sieu_nhan_A.mau_sac = "pink "
# sieu_nhan_A.cai_gi_day = "?????"

# print("ten sieu nhan do la:",sieu_nhan_A.ten)
# print("sieu nhan do mau gi :",sieu_nhan_A.mau_sac)
# print("su dung vu khi:", sieu_nhan_A.vu_khi)
# print("????:",sieu_nhan_A.cai_gi_day)
# print("akakakak:",sieu_nhan_A.aaaaaa)


# class giang:
#     def __init__(self, para_ten , para_vu_khi,para_mau_sac):
#         self.ten = "cristiano "+para_ten
#         self.vu_khi=para_vu_khi
#         self.mau_sac = para_mau_sac
#     # pass
# sieu_nhan_A = giang("Ronaldo","đôi chân ","while")

# print("Ten cua sieu nhan la :" , sieu_nhan_A.ten)
# print("Sieu nhan mau :", sieu_nhan_A.mau_sac)
# print("Su dung vu khi:",sieu_nhan_A.vu_khi)

# class RealMadrid:
#     def __init__(self, para_ten,para_vu_khi,para_mau_sac):
#         self.ten = "giang "+para_ten
#         self.vu_khi = "ak" + para_vu_khi
#         self.mau_sac = para_mau_sac
#     def xin_chao (self):
#         return "xinchao,ta chinh la "+self.ten
# sieu_nhan = RealMadrid("madridista ", "47","gold" )
# print(sieu_nhan.xin_chao())
# print(RealMadrid.xin_chao(sieu_nhan))


# class back:
#     so_thu_tu = 1 
#     suc_manh = 5000
#     def __init__(self, para_ten , para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#         self.stt = back.so_thu_tu
#         back.so_thu_tu += 1 

# call_me_supperman =back("sieu nhan do","kiem","do")
# call_me_supperman_b = back("sieu nhan trắng","sung","trang")
# # # print(back.suc_manh)
# # # print(call_me_supperman.suc_manh)

# # # back.suc_manh = 30 

# # # print(back.suc_manh)
# # # print(call_me_supperman.suc_manh)

# print (call_me_supperman.stt)
# print(call_me_supperman_b.stt)
# print(back.so_thu_tu)


class Sieunhan:
    suc_manh = 60
    def __init__(self,para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def hello(self):
        print("xinchaotala ", self.ten)
        print("sucmanhcuata",self.suc_manh)
        print("vu khi cua ta",self.vu_khi)
sieu_nhan_a = Sieunhan("sieunhando","kiem","do")
sieu_nhan_a.hello()


# class ramos:
#     suc_manh = 50
#     def __init__(self, para_ten, para_so_ao,para_mau_sac):
#         self.ten = para_ten
#         self.so_ao=para_so_ao
#         self.mau_sac = para_mau_sac
#     @classmethod
#     def cap_nhat_suc_manh(cls,smanh):
#         cls.suc_manh=smanh
# real_madrid = ramos("sr","4","red")
#
# print(ramos.suc_manh)
# print(real_madrid.suc_manh)
#
# ramos.cap_nhat_suc_manh(99)

print(ramos.suc_manh)
print(real_madrid.suc_manh)