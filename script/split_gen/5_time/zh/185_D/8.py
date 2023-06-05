def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    B = []
    for i in range(1,M):
        B.append(A[i]-A[i-1]-1)
    B.sort()
    print(sum(B[0:N-M]))
