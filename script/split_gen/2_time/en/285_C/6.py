def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        ans += 26**i
    ans += sum([ord(c) - ord('A') for c in S]) * 26**(N-1)
    print(ans)
