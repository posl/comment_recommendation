def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            if max < abs(a[i]-a[j]):
                max = abs(a[i]-a[j])
    print(max)

if __name__ == '__main__':
    main()