def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)
