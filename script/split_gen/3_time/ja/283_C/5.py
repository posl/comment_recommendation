def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        else:
            if S[i] != '0':
                ans += int(S[i]) + 1
            else:
                ans += 1
    print(ans)
