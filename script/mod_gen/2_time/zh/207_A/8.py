def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == n-1:
            ans += 1
        elif a[i] == a[i+1]:
            ans += 1
        else:
            ans += 2
    print(ans//2)

if __name__ == '__main__':
    main()