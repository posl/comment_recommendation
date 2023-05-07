def main():
    S = input()
    l = len(S)
    ans = 0
    for i in range(l):
        ans += 26**i
    ans += sum([ord(s) - ord("A") + 1 for s in S]) - l
    print(ans)
