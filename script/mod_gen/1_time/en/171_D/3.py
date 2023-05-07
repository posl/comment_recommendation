def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    
    sum_A = sum(A)
    count_B = [0]*10**5
    for i in range(N):
        count_B[A[i]-1] += 1
    for i in range(Q):
        sum_A += (C[i] - B[i]) * count_B[B[i]-1]
        count_B[C[i]-1] += count_B[B[i]-1]
        count_B[B[i]-1] = 0
        print(sum_A)

if __name__ == '__main__':
    main()