def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[i] == a[j]:
            j += 1
        ans += (j - i - 1) * (j - i) // 2
        i = j
    print(ans)

if __name__ == '__main__':
    main()