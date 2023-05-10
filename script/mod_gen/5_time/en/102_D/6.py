def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    min_diff = 10 ** 9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                B = A[0:i]
                C = A[i:j]
                D = A[j:k]
                E = A[k:N]
                P = sum(B)
                Q = sum(C)
                R = sum(D)
                S = sum(E)
                max_val = max(P, Q, R, S)
                min_val = min(P, Q, R, S)
                diff = max_val - min_val
                if diff < min_diff:
                    min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()