def main():
    H = int(input())
    ans = 0
    while H > 0:
        H //= 2
        ans += 1
    print(2 ** ans - 1)
