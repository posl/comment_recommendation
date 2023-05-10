def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if a[i] % a[i-1] != 0:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()