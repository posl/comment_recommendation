def main():
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    n, m = 20, 20
    a = [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]
    a.sort()
    a.append(m)
    ans = 0
    i = 0
    while i < n:
        j = i
        while a[j] == a[j + 1]:
            j += 1
        ans += (a[j] - a[i]) // (m + 1)
        i = j + 1
    print(ans)

if __name__ == '__main__':
    main()