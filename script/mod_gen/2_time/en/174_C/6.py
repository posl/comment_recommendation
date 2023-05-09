def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    ans = 1
    s = 7
    while True:
        if s % k == 0:
            print(ans)
            return
        s = (s * 10 + 7) % k
        ans += 1

if __name__ == '__main__':
    main()