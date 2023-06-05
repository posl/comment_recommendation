def main():
    n = int(input())
    ans = 0
    while 2 ** ans <= n:
        ans += 1
    print(ans - 1)
main()
