def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    i = 0
    j = k - 1
    ans = 0
    while j < n:
        ans += 1
        i += k
        j += k
        while j < n and a[i] == a[j]:
            i += 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()