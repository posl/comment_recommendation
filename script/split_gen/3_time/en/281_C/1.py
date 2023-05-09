def main():
    N, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    sumA = sum(A)
    t = T % sumA
    for i in range(N):
        if t < A[i]:
            print(i+1)
            print(t)
            break
        t -= A[i]
