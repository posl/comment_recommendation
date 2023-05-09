def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    median = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i] - median)
    print(ans)

if __name__ == '__main__':
    main()