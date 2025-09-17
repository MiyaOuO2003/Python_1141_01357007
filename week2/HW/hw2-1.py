n = int(input("請輸入三角形的高度:"))
if n <= 0:
    print("輸入錯誤")
else:
    for i in range (n):
        for j in range (n + i):
            if j == n - 1 - i or j == n - 1 + i or i == n - 1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()