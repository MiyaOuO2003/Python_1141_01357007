n = int(input("請輸入 n:\n"))
arr = []
print("請輸入數列:\n", end="")
arr = list(map(int, input().split()))
print("排序前的數列:", ' '.join(map(str ,arr)), end="")
print(" ")
arr.sort()
print("排序後的數列:", ' '.join(map(str ,arr)))