def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    cnt = 0
    ans = [0] * (max_a + 1)
    for i in range(n):
        ans[a[i]] += 1
    for i in range(1, max_a + 1):
        if ans[i] == 1:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()