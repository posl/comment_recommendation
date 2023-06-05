def solve():
    N = int(input())
    S = input()
    s = S[0]
    count = 1
    for i in range(1,N):
        if s != S[i]:
            s = S[i]
            count += 1
    print(count)
