def solve():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_idx = a.index(a_max)
    a.pop(a_max_idx)
    for i in range(n):
        print(a_max if i != a_max_idx else max(a))

if __name__ == '__main__':
    solve()