def main():
    S = input()
    N = len(S)
    if N == 1:
        print(int(S))
        return
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i]) - 1
        else:
            ans += int(S[i])
    ans += N - 1
    print(ans)
