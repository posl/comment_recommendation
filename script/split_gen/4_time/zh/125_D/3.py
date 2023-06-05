def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += abs(A[i])
    if A[0] < 0:
        sum -= 2 * A[0]
    elif A[-1] > 0:
        sum -= 2 * A[-1]
    print(sum)
