def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] != a[i+1]:
            if cnt >= a[i]:
                ans += cnt - a[i]
            else:
                ans += cnt
            cnt = 1
        else:
            cnt += 1
    print(ans)

if __name__ == '__main__':
    main()