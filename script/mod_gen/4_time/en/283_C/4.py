def solve():
    S = input()
    N = len(S)
    ans = N-1
    for i in range(1, 1<<N):
        t = 0
        for j in range(N):
            if i&(1<<j):
                t = t*10+int(S[j])
        if t%3==0:
            ans = min(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    solve()