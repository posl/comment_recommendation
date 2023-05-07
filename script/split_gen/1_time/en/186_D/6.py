def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    sum = 0
    for i in range(0, N):
        sum += A[i] * (i+1) - A[i] * (N-i-1)
    print(sum)
