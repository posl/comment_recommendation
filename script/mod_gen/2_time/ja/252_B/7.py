def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()
    for i in range(k):
        if a[i] <= b[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()