def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i]-a[j]) > max:
                max = abs(a[i]-a[j])
    print(max)

if __name__ == '__main__':
    main()