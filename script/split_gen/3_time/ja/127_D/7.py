def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    
    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1], reverse=True)
    
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        i += 1
    
    print(sum(A))
