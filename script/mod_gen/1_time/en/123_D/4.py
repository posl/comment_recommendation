def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ans = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                ans.append(a[i] + b[j] + c[k])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

if __name__ == '__main__':
    main()