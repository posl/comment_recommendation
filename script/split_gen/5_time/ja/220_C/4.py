def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    X = int(input())
    a_sum = sum(A)
    if X < a_sum:
        print(0)
    else:
        k = (X // a_sum) * N
        X = X % a_sum
        for i in range(N):
            if X < 0:
                break
            X -= A[i]
            k += 1
        print(k)
