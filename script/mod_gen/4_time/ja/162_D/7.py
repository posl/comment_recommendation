def solve():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]: continue
            k = j + (j - i)
            if k >= N: continue
            if S[i] == S[k] or S[j] == S[k]: continue
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()