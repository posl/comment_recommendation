def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print("")
    city = [0] * N
    for i in range(M):
        city[A[i]-1] += 1
        city[B[i]-1] += 1
    #print(city)
    #print("")
    for i in range(N):
        print(city[i])
