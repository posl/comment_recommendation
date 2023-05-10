def main():
    x, y, z, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ans = []
    for i in range(x):
        for j in range(y):
            for l in range(z):
                ans.append(a[i] + b[j] + c[l])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

if __name__ == '__main__':
    main()