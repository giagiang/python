# g = 6 
# while g > 0 :
#     print('g=', g )
#     g -=1


# a = 'ricciardo' 
# ids = 0 
# length = len(a)

# while ids < length:
#     print(ids, 'stands for', a[ids]) 
#     ids += 1

# mot_so_nao_do = []
# ko_so = 1

# while True:
#     if ko_so % 2 == 0:
#         mot_so_nao_do.append(ko_so)
#         if len(mot_so_nao_do) >= 50 :
#             break
#     ko_so += 1 
# print(mot_so_nao_do)
# print(ko_so)          


# so_nao_do = 1
# while so_nao_do < 10:
#     if so_nao_do % 2 == 0 :
#         so_nao_do += 1 
#         continue
#     print(so_nao_do, 'la mot so ')
#     so_nao_do +=1
# print(so_nao_do)


# so_a = 0 
# while so_a < 10 :
#     so_a += 1 
#     if so_a % 2 == 0:
#         continue
#     print(so_a,'asdasdsa')
# print(so_a)   

# g = 0 
# while g < 4 :
#     print('g ddang nhir hown boong',g )
#     g += 1 
# else:
#     print('g lon hon 4 ')    
# bài tập
# #1
# so_nam = []
# k_a = 1

# while len(so_nam) < 5:
#     if k_a % 2 == 0:
#         so_nam.append(k_a)   
#     k_a += 1     

# 2


# with open('draft.txt') as f:
#     # lấy nội dung của file dưới dạng một list
#     data = f.readlines()

# idx = 0 # mốc bắt đầu
# length = len(data) # mốc kết thúc
# new_content = '' # nội dung mới sẽ ghi vào file mới

# while idx < length:
#     # tách một dòng thành một list
#     line_list = data[idx].split()
#     idline = 0
#     length_line = len(line_list)
#     while idline < length_line:
#         if line_list[idline] == 'Kteam':
#             # thay thế chữ trước Kteam là How
#             line_list[idline - 1] = 'How'
#         idline += 1
#     # nối lại thành một dòng chuỗi
#     new_content += ' '.join(line_list) + '\n'
#     idx += 1

# with open('kteam.txt', 'w') as new_f:
#     # ghi nội dung mới vào file kteam.txt
#     new_f.write(new_content)


# a = 3 
# b = 9 

# c = 0 
# while a <= b:
#     if a % 2 !=0:
#         c += a # c = 3, 3, 8, 8, 15, 15, 24
#     a += 1 # a = 4, 5, 6, 7, 8, 9
# print(c) 



# s = "databasesystem"
# for c in s:
#     if c == 'y':
#         continue
#     print("Current character:", c)

# a = "ricciardo"
# for b in a :
#     if b =='d':
#         continue
#     print("dasdasd:",b)    

# a = 100 
# b = 10 
# c = 0 
# while b <= a :
#     c += b 
#     b+=1
# print(c)    

# n = 2
# i = 1
# answer = 0
# while i <= n:
#     print("i value: ", i)
#     print("answer value: ", answer)
#     print("_____________")
#     answer = answer +  i
#     i = i + 1
# print(answer)


n = 5
i = 1
answer = 0
while i <= n:
    answer += i
    i += 1
    print('1', i)
print(answer)

# //1
# ans: 1
# i: 2
# //
# ans: 3
# i: 3
# // 
# ans: 6
# i: 4
# //
# ans: 10
# i: 5
# // 15
# // 5 