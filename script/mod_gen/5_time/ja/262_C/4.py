def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    ans = 0
    for i in range(n-1):
        if b[i] > b[i+1]:
            ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()