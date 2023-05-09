def main():
    a, b, k = map(int, input().split())
    c = min(a, b)
    ans = 0
    while c > 0:
        if a % c == 0 and b % c == 0:
            k -= 1
            if k == 0:
                ans = c
                break
        c -= 1
    print(ans)
main()

if __name__ == '__main__':
    main()