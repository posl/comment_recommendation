def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(1,N):
        if S[i] == S[i-1]:
            ans += 1
    print(ans)
