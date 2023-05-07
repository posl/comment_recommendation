def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = ['No'] * N
    for i in range(N):
        if S[i] in T:
            ans[i] = 'Yes'
    print(*ans, sep='
')
    return
