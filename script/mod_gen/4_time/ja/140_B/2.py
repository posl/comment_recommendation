def main():
    n = int(input())
    a = [int(i)-1 for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]]
        if i != n-1 and a[i]+1 == a[i+1]:
            ans += c[a[i]]
    print(ans)

if __name__ == '__main__':
    main()