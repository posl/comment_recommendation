def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    B = [0] * N
    #print(B)
    for i in range(N):
        B[A[i]-1] += 1
    #print(B)
    for i in range(N):
        print(B[i])
main()
