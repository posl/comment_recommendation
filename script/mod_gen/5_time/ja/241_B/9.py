def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if m > n:
        print("No")
    else:
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] <= b[j]:
                i = i + 1
                j = j + 1
            else:
                i = i + 1
        if j == m:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()