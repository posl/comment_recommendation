def main():
    n, x = map(int, input().split())
    ans = ""
    for i in range(n):
        ans += chr(65 + i) * n
    print(ans[x - 1])
