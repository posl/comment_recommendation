def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] == '0' and S[i - 1] == '1':
            ans += 1
    if ans == N - 1:
        print(N)
        exit()
    if ans == 0:
        print(0)
        exit()
    ans += 1
    for i in range(N):
        if S[i] == '1':
            W[i] = 0
    L = []
    for i in range(N):
        if S[i] == '0':
            L.append(W[i])
    L.sort()
    ans += L[-1]
    print(ans)
