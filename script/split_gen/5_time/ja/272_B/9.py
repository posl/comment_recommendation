def main():
    n, m = map(int, input().split())
    p = [0] * n
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in x:
            p[i - 1] += 1
    for i in p:
        if i == 0:
            print('No')
            return
    print('Yes')
