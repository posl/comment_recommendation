def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (26 ** (i)) * (ord(S[len(S) - 1 - i]) - 64)
    print(ans)
