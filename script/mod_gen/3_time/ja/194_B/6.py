def main():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

if __name__ == '__main__':
    main()