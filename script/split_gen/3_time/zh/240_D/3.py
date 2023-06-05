def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i])
        while len(b) > 1:
            if b[-1] == b[-2]:
                b.pop()
                b.pop()
            else:
                break
        print(len(b))
