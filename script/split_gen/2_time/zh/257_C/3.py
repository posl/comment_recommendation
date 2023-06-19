def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if S[i] == '1':
            ans += W[i]
    # print(ans)
    c = 0
    for i in range(N):
        if S[i] == '1':
            c += W[i]
    # print(c)
    ans = max(ans, c)
    c = 0
    for i in range(N):
        if S[i] == '0':
            c += W[i]
    # print(c)
    ans = max(ans, c)
    print(ans)
