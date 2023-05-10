def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    even = []
    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
    if len(even) == 0:
        print(-1)
        return
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return
main()

if __name__ == '__main__':
    main()