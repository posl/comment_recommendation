def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    num = 1
    for i in range(n):
        if a[i] == a[i+1]:
            num += 1
        else:
            ans += (n-i-1)*(n-i-2)//2*num
            num = 1
    print(ans)

if __name__ == '__main__':
    main()