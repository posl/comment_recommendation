def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    aoki = sum(a)
    takahashi = 0
    for i in range(n):
        if a[i] < b[i]:
            takahashi += b[i] - a[i]
    print(takahashi)
