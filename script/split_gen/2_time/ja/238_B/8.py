def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(N):
        A[i] = 360 - A[i]
    #print(A)
    for i in range(N):
        for j in range(i+1, N):
            A[i] = A[i] % A[j]
    print(A[0])
