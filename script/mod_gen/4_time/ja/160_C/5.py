def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    ans = k
    for i in range(n):
        ans = min(ans, k-(a[i+1]-a[i]))
    print(ans)

if __name__ == '__main__':
    main()