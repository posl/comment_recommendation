def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[i] - (i+1) for i in range(n)]
    b.sort()
    if n % 2 == 1:
        x = b[n//2]
    else:
        x = (b[n//2-1] + b[n//2]) // 2
    print(sum([abs(b[i]-x) for i in range(n)]))

if __name__ == '__main__':
    main()