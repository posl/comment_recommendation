def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(tuple(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if A[i] < c:
                A[i] = c
                i += 1
            else:
                break
            if i == N:
                break
        if i == N:
            break
    print(sum(A))
