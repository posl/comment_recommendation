def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

if __name__ == '__main__':
    main()