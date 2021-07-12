stu = (int(input("請輸入學生的數量: ")))
score = []
summ = 0
high = 0
low = 100
ln = "no"
hn = "no"
for i in range(stu):
    c = (int(input("請輸入學生的成績: ")))
    name = (input("請輸入學生的名子: "))
    score.append(c)
    summ = summ + c
    if high < c:
        high = c
        hn = name
    if low > c:
        low = c
        ln = name
avg = summ/stu
print("全班總分:", summ, "分")
print("全班平均:",avg,"分")
print("全班最低分:",low,"分",ln)
print("全班最高分:",high,"分",hn)