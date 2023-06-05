def problem129_b():
    N = int(input())
    W = list(map(int,input().split()))
    min = 100000
    for i in range(1,N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        if abs(s1-s2) < min:
            min = abs(s1-s2)
    print(min)
problem129_b()
