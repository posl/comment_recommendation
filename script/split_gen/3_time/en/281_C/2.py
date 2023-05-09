def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    i = T % sumA
    for j in range(N):
        i -= A[j]
        if i < 0:
            print(j + 1, A[j] + i)
            break
