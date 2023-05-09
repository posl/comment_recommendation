def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += 1
        H //= 2
    print(2**ans - 1)
main()
