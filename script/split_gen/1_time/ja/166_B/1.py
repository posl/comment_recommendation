def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    #print(n, k, d, a)
    s = set()
    for i in range(k):
        for j in range(d[i]):
            s.add(a[i][j])
    print(n - len(s))
