def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    if M == 0:
        print(1)
        return
    k = min([b for b in B if b > 0])
    for b in B:
        if b > 0:
            k = gcd(k, b)
    print((max(B) + k - 1) // k)
