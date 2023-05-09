def main():
    P = list(map(int, input().split()))
    ans = ""
    for p in P:
        ans += chr(ord("a") + p - 1)
    print(ans)
