def main():
    S = input()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = 0
    for i in range(len(S)):
        ans += alpha.index(S[i]) * (26 ** (len(S) - i - 1))
    print(ans + 1)
