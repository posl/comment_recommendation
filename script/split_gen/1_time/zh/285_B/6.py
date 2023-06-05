def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        ans = 0
        while i + ans < n and s[ans] != s[i + ans]:
            ans += 1
        print(ans)
