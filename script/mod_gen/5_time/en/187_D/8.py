def solve():
    N = int(input())
    towns = []
    for i in range(N):
        A, B = map(int, input().split())
        towns.append((A, B))
    towns.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = sum(x[0] for x in towns)
    takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += towns[i][0]
        else:
            aoki -= towns[i][0]
    print(takahashi - aoki)

if __name__ == '__main__':
    solve()