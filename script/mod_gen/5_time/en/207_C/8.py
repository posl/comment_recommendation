def main():
    n = int(input())
    a = []
    for _ in range(n):
        t,l,r = map(int, input().split())
        if t == 2 or t == 4:
            r -= 0.1
        if t == 3 or t == 4:
            l += 0.1
        a.append((l,r))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i][0] <= a[j][1] and a[j][0] <= a[i][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()