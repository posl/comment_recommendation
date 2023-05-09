def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(len(bin(n)[2:]))
        return
    if a == 10:
        print(len(str(n)))
        return
    if n % a == 1:
        print(1)
        return
    ans = 1
    x = 1
    while True:
        x = x * a % n
        ans += 1
        if x == 1:
            print(ans)
            return
        if ans > n:
            print(-1)
            return
main()
The code is written in Python3.

if __name__ == '__main__':
    main()