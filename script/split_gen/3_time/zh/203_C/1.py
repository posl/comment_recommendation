def main():
    N, K = map(int, input().split())
    d = {}
    for i in range(N):
        A, B = map(int, input().split())
        if A not in d:
            d[A] = B
        else:
            d[A] += B
    d = sorted(d.items(), key=lambda x:x[0])
    for i in range(len(d)):
        if d[i][0] > K:
            break
        else:
            K += d[i][1]
    print(K)
