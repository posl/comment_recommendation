def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        d_i = int(input())
        A = list(map(int, input().split()))
        for j in range(d_i):
            d[A[j]-1] += 1
    print(d.count(0))
