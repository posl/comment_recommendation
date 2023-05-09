def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - (i+1))
    b.sort()
    b1 = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i]-b1)
    print(ans)

if __name__ == '__main__':
    main()