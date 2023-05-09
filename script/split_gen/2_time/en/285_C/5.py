def main():
    S = input()
    L = len(S)
    ans = 0
    for i in range(L):
        ans += (ord(S[i]) - ord('A') + 1) * 26 ** (L - i - 1)
    print(ans)
