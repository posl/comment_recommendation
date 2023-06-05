def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a
    ans = 0
    for i in range(1,n+1):
        if a[i] == i:
            for j in range(i+1,n+1):
                if a[j] == j:
                    ans += 1
        else:
            if a[a[i]] == i:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()