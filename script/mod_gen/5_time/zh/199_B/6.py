def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1000):
        flag = True
        for j in range(n):
            if i < a[j] or b[j] < i:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()