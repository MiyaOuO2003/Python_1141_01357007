n = int(input())
for i in range(n):
    str = input()
    char = dict()
    for j in str:
        if j in char:
            char[j] += 1
        else:
            char[j] = 1
    print(max(char, key=char.get))
