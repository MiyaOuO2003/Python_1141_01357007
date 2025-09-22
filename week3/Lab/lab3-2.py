N = int(input())
while True:
    if N == 0:
        break
    while True:
        target = input().strip()
        if target == "0":
            exit()
        target = list(map(int, target.split(' ')))
        if len(target) != N:
            break
        stack = []
        idx = 0
        for i in range(1, N + 1):
            stack.append(i)
            while stack and stack[-1] == target[idx]:
                stack.pop()
                idx += 1
        if idx == N:
            print("YES")
        else:
            print("NO")
