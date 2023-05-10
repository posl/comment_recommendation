def solve():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append((A[i], B[i], i+1))
    AB.sort(key=lambda x: x[2])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)
    AB = AB[:X+Y+Z]
    AB.sort(key=lambda x: x[2])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)
    for a, b, i in AB:
        print(i)
