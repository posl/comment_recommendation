def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()