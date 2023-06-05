def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        return
    # 1. find max A_i
    maxA = max(A)
    maxA_idx = A.index(maxA)
    # 2. find max A_i in the range [maxA_idx+1, N-1]
    maxA2 = max(A[maxA_idx+1:])
    # 3. find max A_i in the range [0, maxA_idx-1]
    maxA3 = max(A[:maxA_idx])
    print(maxA + max(maxA2, maxA3))
