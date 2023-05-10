def solve():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: sum(x), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()