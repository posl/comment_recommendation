def solution():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    for i in range(1, 100):
        if x - i not in p:
            print(x - i)
            return
        elif x + i not in p:
            print(x + i)
            return
solution()
