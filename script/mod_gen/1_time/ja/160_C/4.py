def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    max = 0
    for i in range(n-1):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    if max < a[0] + k - a[n-1]:
        max = a[0] + k - a[n-1]
    print(k - max)

if __name__ == '__main__':
    main()