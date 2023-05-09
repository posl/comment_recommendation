def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        a = list(map(int, input().split()))
        for j in range(a[0]):
            d[a[j + 1] - 1] += 1
    print(d.count(0))
