def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, T)
    # print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
        if T <= sum:
            print(i+1, T - (sum-A[i]))
            break
