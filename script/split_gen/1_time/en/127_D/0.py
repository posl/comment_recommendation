def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N or A[i] >= c:
                break
            A[i] = c
            i += 1
    print(sum(A))
