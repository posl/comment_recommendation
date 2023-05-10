def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    min_distance = 10**9
    for i in range(n):
        for j in range(m):
            if abs(a[i]-b[j]) < min_distance:
                min_distance = abs(a[i]-b[j])
    print(min_distance)

if __name__ == '__main__':
    main()