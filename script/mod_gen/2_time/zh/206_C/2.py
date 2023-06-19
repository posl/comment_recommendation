def count_pair():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] != a[i+1]:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
        else:
            cnt += 1
    print(ans)

if __name__ == '__main__':
    count_pair()