def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    sum_min = sum
    for i in range(N):
        for j in range(N):
            sum_tmp = sum
            for k in range(i):
                sum_tmp -= L
            for k in range(N-j, N):
                sum_tmp -= R
            if i < j:
                sum_tmp += (j-i) * L
            elif i > j:
                sum_tmp += (i-j) * R
            if sum_tmp < sum_min:
                sum_min = sum_tmp
    print(sum_min)
