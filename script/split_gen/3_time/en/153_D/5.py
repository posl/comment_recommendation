def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += 1
        H >>= 1
    print(ans)
