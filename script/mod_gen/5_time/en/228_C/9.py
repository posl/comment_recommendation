def problems228_c():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    print('Yes' if k <= sum(sorted([sum(p[i]) for i in range(n)], reverse=True)[:k]) else 'No')

if __name__ == '__main__':
    problems228_c()