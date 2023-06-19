def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, M, A)
    # print(len(A))
    max_sum = 0
    for i in range(0, len(A)-M+1):
        # print(i)
        # print(A[i:i+M])
        sum = 0
        for j in range(0, M):
            sum += (j+1) * A[i+j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)
