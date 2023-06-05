def solve():
    n, k = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    scores.sort(key=lambda x: sum(x), reverse=True)
    for i in range(n):
        if i < k:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()