def main():
    n, x = map(int, input().split())
    ans = ""
    for i in range(26):
        if n * (i + 1) >= x:
            ans = chr(65 + i)
            break
    print(ans)
