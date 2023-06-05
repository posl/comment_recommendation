def main():
    N, X = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, 1 << N):
        product = 1
        for j in range(N):
            if i >> j & 1:
                product *= A[j][0]
        if product == X:
            ans += 1
    print(ans)
