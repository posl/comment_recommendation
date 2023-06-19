def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a)
    cnt = [0] * 10**5
    for i in range(n):
        cnt[a[i]-1] += 1
    for i in range(q):
        sum_a += (bc[i][1]-bc[i][0]) * cnt[bc[i][0]-1]
        cnt[bc[i][1]-1] += cnt[bc[i][0]-1]
        cnt[bc[i][0]-1] = 0
        print(sum_a)

if __name__ == '__main__':
    solve()