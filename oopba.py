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

# print(ramos.suc_manh)
# print(real_madrid.suc_manh)

# ramos.cap_nhat_suc_manh(99)

# print(ramos.suc_manh)
# print(real_madrid.suc_manh)


# class SieuNhan:
#     suc_manh = 50
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#     @classmethod
#     def from_string(cls, s): # thường những phương thức xử lí thế này hay có tên là from…
#         lst = s.split('-')
#         new_lst = [st.strip() for st in lst]
#         ten, vu_khi, mau_sac = new_lst
#         return cls(ten, vu_khi, mau_sac)

# infor_str = "Sieu nhan do - Kiem - Do"
# sieu_nhan_A = SieuNhan.from_string(infor_str)
# print(sieu_nhan_A.__dict__)\


# class SieuNhan:
#     suc_manh = 50
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#     @classmethod
#     def cap_nhat_suc_manh(cls, smanh):
#         cls.suc_manh = smanh
# sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)

# SieuNhan.cap_nhat_suc_manh(40)

# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)


# s= "giagiang - beo - rad - krae"
# lst = s.split("-")
# print(lst)
        
# new_value = [x.strip() for x in lst]
# print(new_value)        

# a = "gì do - chao - krate"
# lst = a.split("-")
# print(lst)

# newlst = [b.strip()for b in lst]
# print(newlst)


class Mec :
    suc_manh = 750 
    def __init__(self, para_ten , para_mau_sac , para_toc_do):
        self.ten = para_ten
        self.mau_sac = para_mau_sac
        self.toc_do = para_toc_do
    @classmethod
    def from_string(cls , s):
        st = s.split('-')
        new_lst = [b.strip()for b in st]
        ten,mau_sac,_toc_do = new_lst
        return cls(ten, mau_sac, _toc_do)

infor = "G class - black - 200"
oto  = Mec.from_string(infor) 
print(oto.__dict__)           

# class sieuNhan:
#     suc_manh = 50 
#     def __init__(self , para_ten , para_vu_khi , para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#     @staticmethod
#     def bien_hinh():
#         print("1,2,3. Sieu nhan bien hinh")

# sieu_nhan_A = sieuNhan("Sieu nhan do","kiem","do")
# sieu_nhan_A.bien_hinh()    


# class SieuNhan:
#     suc_manh = 50
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#     @classmethod
#     def cap_nhat_suc_manh(cls, smanh):
#         cls.suc_manh = smanh
# sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)

# SieuNhan.cap_nhat_suc_manh(40)

# print(SieuNhan.suc_manh)
# print(sieu_nhan_A.suc_manh)