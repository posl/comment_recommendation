def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    sum_A = sum(A)
    sum_B = sum_A * (X // sum_A)
    count = N * (X // sum_A)
    for i in range(N):
        sum_B += A[i]
        count += 1
        if sum_B > X:
            break
    print(count)
