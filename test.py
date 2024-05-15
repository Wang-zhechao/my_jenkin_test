str_1 = "abcdefghijklmnop"
str_2 = "abcsafjklmnopqrstuvw"
if len(str_1) > len(str_2):
    str_1, str_2 = str_2, str_1

for l in range(len(str_1), 1, -1):
    for i in range(0, len(str_1)-l):
        print(str_1[i:i+l])
