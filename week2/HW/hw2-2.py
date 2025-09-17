arr = []
n = 0
try:
    while True:
        arr.append(int(input("請輸入一個數:")))
        n += 1
        arr.sort()
        if n % 2:
            print(arr[n // 2])
        else:
            print((arr[n // 2 - 1] + arr[n // 2]) // 2)
except EOFError:
    pass