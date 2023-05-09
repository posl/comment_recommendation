def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            ans += 1
    print(n - ans)
main()

if __name__ == '__main__':
    main()