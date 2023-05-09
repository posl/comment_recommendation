def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B = list(filter(lambda x: x > 0, B))
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    for b in B:
        k = gcd(k, b)
    print((max(B) + k - 1) // k)
