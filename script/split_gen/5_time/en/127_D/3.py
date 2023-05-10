def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for _ in range(M):
        b, c = map(int, input().split())
        BC.append((b, c))
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N:
                break
            if A[i] < c:
                A[i] = c
            else:
                break
            i += 1
    print(sum(A))
