def solve():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    if j - i != k - j:
                        cnt += 1
    print(cnt)
