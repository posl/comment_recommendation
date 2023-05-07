def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    sum = 0
    for i in range(N):
        sum += abs(A[i] - (i+1))
    print(sum)
