def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > r:
            break
        for j in range(i, n):
            if a[j] > q:
                break
            for k in range(j, n):
                if a[k] > p:
                    break
                for l in range(k, n):
                    if a[l] > r:
                        break
                    if i <= j <= k <= l:
                        if a[i] + a[j] + a[k] == p and a[j] + a[k] + a[l] == q and a[i] + a[k] + a[l] == r:
                            ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()