def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(i)-1 for i in input().split()]
    cnt = [0] * n
    for i in c:
        cnt[b[i]] += 1
    ans = 0
    for i in range(n):
        ans += cnt[a[i]]
    print(ans)

if __name__ == '__main__':
    main()