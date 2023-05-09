def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    print(N - ans if ans != N else -1)
main()

if __name__ == '__main__':
    main()