def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    min = 10**9
    for i in range(n):
        for j in range(m):
            if min > abs(a[i] - b[j]):
                min = abs(a[i] - b[j])
    print(min)

if __name__ == '__main__':
    main()