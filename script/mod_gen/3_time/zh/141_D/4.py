def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(m):
        a.append(a.pop()//2)
    print(sum(a))

if __name__ == '__main__':
    solve()