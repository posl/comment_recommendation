def main():
    N = int(input())
    A = list(map(int, input().split()))
    minus = 0
    min_num = 10**9 + 1
    sum = 0
    for i in range(N):
        sum += abs(A[i])
        if A[i] < 0:
            minus += 1
        if abs(A[i]) < min_num:
            min_num = abs(A[i])
    if minus % 2 == 0:
        print(sum)
    else:
        print(sum - 2*min_num)
