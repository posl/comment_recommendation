def solve():
    N = int(input())
    shops = []
    for _ in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    shops.sort(key=lambda x: x[0])
    for A, P, X in shops:
        if X > A:
            return P
    return -1
print(solve())

if __name__ == '__main__':
    solve()