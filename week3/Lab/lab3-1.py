n, m = map(int, input().split())

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

setintersection = sorted(setA & setB)
if len(setintersection) != 0:
    print(len(setintersection))
    print(' '.join(map(str, setintersection)))