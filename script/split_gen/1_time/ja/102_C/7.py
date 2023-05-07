def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    #print(A)
    #print(N)
    #print(A)
    if N % 2 == 0:
        b = (A[N//2] + A[N//2-1]) / 2
    else:
        b = A[N//2]
    #print(b)
    sum = 0
    for i in range(N):
        sum += abs(A[i] - (b + i))
    print(int(sum))
