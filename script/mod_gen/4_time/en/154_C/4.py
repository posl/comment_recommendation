def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i] == a[i-1]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()