def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, 10**5 + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) // 2
    for a in A:
        if cnt[a] >= 2:
            print(ans - (cnt[a] - 1))
        else:
            print(ans)

if __name__ == '__main__':
    main()