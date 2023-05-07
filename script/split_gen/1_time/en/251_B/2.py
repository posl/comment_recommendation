def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for a in range(N + 1):
        for b in range(N + 1):
            for c in range(N + 1):
                for d in range(N + 1):
                    for e in range(N + 1):
                        for f in range(N + 1):
                            for g in range(N + 1):
                                if a + b + c + d + e + f + g > N:
                                    continue
                                if a * A[0] + b * A[1] + c * A[2] + d * A[3] + e * A[4] + f * A[5] + g * A[6] <= W:
                                    ans += 1
    print(ans)
