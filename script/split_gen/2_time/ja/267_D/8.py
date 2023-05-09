def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    B = []
    for i in range(N):
        for j in range(i, N):
            B.append(sum(A[i:j+1]))
    print(B)
