def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    n = len(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += n - j - 1
    print(ans)
main()

if __name__ == '__main__':
    main()