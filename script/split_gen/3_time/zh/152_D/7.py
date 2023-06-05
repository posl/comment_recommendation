def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        ans += len(s) % 2
        if s[0: len(s) // 2] == s[len(s) // 2: len(s)][::-1]:
            ans += 1
    print(ans)
