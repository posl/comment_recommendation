def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        while i % 2 == 0:
            i = i // 2
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()