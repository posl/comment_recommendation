def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in A:
        while i % 2 == 0:
            ans += 1
            i //= 2
    print(ans)

if __name__ == '__main__':
    main()