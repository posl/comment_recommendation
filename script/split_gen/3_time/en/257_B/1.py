def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [0] * n
    for i in range(q):
        l[int(input()) - 1] += 1
    for i in range(n):
        if a[i] + l[i] >= q + 1:
            print('Yes')
        else:
            print('No')
