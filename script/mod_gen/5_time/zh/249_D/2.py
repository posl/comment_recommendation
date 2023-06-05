def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    max_a = max(a)
    #print(max_a)
    cnt = [0]*(max_a+1)
    for i in range(1, n+1):
        cnt[a[i]] += 1
    #print(cnt)
    ans = 0
    for i in range(1, max_a+1):
        for j in range(i, max_a+1, i):
            if cnt[j] == 0:
                continue
            if i == j:
                ans += cnt[i]*(cnt[i]-1)*(cnt[i]-2)//6
            elif i < j:
                k = j-i
                if k > max_a:
                    continue
                ans += cnt[i]*cnt[j]*cnt[k]
    print(ans)
    return

if __name__ == '__main__':
    main()