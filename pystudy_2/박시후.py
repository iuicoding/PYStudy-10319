score = int(input("입력"))

if score == 100:
    print("만족")
elif 90 < score:
    print("만족")
elif 80 < score:
    print("만족")
elif 70 < score:
    print("불만족")
elif 60 < score:
    print("매우 불만족")
alist = [1,2,3,4,5]
print(alist)

if 7 in alist:
    print("7가 있네")

if 111 not in alist:
    print("111없음 뭐임")

    print(alist[1])

alsit = alist +[4]
alist = alist +5
alist .append(9)
print(alist)

del alist[1]
alist.remove(3)
alist.pop(7)
alist.pop()
print(alist)

print(alist+[5])
print(alist * 8)

for element in alist:
    print(element)