def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0]*(n+1)
    for i in range(n):
        l[a[i]] = i+1
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if l[i] > l[j]:
                break
            if l[i] < l[j] and l[j] < j:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()