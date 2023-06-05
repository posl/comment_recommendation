def count_num():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    num = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            num += 1
    print(num)
