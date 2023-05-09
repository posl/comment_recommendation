def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    median = A[int(N/2)]
    sum = 0
    for i in range(N):
        sum += abs(A[i]-median)
    print(sum)
