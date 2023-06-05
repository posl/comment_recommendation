def solve():
    #n = int(input())
    #a = list(map(int,input().split()))
    n = 5
    a = [5,5,5,5,5]
    ans = 0
    for i in range(1,2**n):
        sum = 0
        cnt = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j]
                cnt += 1
        if sum%cnt == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()