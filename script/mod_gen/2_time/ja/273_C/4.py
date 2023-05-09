def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a.append(0)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += n - cnt
            cnt = 1
    for i in range(n):
        print(ans - (n - i - 1))

if __name__ == '__main__':
    main()