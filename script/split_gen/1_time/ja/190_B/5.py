def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and D < Y:
            print("Yes")
            return
    print("No")
