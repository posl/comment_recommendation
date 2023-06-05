def main():
    a, b, k = map(int, input().split())
    ans = 0
    while a < b:
        a *= k
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()