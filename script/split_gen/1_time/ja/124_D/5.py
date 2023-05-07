def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            if S[i] == '0':
                ans = 1
            else:
                ans = 0
        else:
            if S[i] == '0':
                ans += 1
            else:
                ans = 0
        if ans >= K:
            print(N)
            exit()
    print(ans)
