def solve():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    diff_count = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            diff_count += 1
    if diff_count <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()