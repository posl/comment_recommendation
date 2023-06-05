def main():
    N,T = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = sum(A)
    T = T % sumA
    sumA = 0
    for i in range(N):
        sumA += A[i]
        if sumA >= T:
            print(i+1,T)
            exit()
