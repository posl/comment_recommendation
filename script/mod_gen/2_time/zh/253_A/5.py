def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (max(a)+1)
    for v in a:
        cnt[v] += 1
    ans = 0
    for i in range(len(cnt)):
        if cnt[i] >= 3:
            ans += cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6
        if cnt[i] >= 2:
            for j in range(i+1, len(cnt)):
                if cnt[j] >= 2:
                    ans += cnt[i] * (cnt[i]-1) // 2 * cnt[j] * (cnt[j]-1) // 2
                if cnt[j] >= 1:
                    for k in range(j+1, len(cnt)):
                        if cnt[k] >= 1:
                            ans += cnt[i] * cnt[j] * cnt[k]
    print(ans)

if __name__ == '__main__':
    main()