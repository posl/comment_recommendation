def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p = [[sum(p[i]), p[i][0]] for i in range(n)]
    p.sort(reverse=True)
    for i in range(n):
        if p[i][1] + p[k-1][0] < p[k-1][0]:
            print('No')
        else:
            print('Yes')
