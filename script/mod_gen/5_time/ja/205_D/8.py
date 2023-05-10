def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    ans = []
    for i in range(q):
        ans.append(k[i] + i)
    for i in range(q):
        if ans[i] <= a[0]:
            ans[i] = ans[i] + n - 1
            continue
        if ans[i] >= a[n - 1]:
            ans[i] = ans[i] + n
            continue
        for j in range(n - 1):
            if a[j] < ans[i] and ans[i] <= a[j + 1]:
                ans[i] = ans[i] + j + 1
                break
    for i in range(q):
        print(ans[i])

if __name__ == '__main__':
    main()