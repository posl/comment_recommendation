def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%200 for i in a]
    a.sort()
    ans = 0
    tmp = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            tmp += 1
        else:
            ans += tmp*(tmp+1)//2
            tmp = 0
    ans += tmp*(tmp+1)//2
    print(ans)

if __name__ == '__main__':
    main()