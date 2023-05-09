def main():
    N, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A_sum = sum(A)
    r = T % A_sum
    for i in range(N):
        if r < A[i]:
            print(i+1, r)
            break
        r -= A[i]
