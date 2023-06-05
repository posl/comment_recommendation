def main():
    # input
    S = input()
    K = int(input())
    # initialization
    N = len(S)
    S = S + 'X'
    cnt = 0
    ans = 0
    # count the number of X
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 0
    ans += cnt // 2
    # output
    print(min(ans + K, N - 1))
