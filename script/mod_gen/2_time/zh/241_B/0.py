def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        print("No")
        return
    a.sort()
    b.sort()
    for i in range(m):
        if b[i] <= a[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()