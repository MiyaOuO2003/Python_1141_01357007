n = int(input('請輸入矩陣高度:'))
num = int(1)
print()
if(n <= 0):
    print('輸入錯誤')
else:
    max_num = n * (n + 1) // 2
    width = len(str(max_num)) 
    for i in range(n):
        for j in range(i + 1):
            print(f"{num:>{width}}", end=" ")
            num += 1
        print()
