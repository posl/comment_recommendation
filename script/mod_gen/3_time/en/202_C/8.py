def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = [0] * (N + 1)
    for j in range(N):
        B_C[C[j]] += 1
    A_B_C = [0] * (N + 1)
    for i in range(N):
        A_B_C[A[i]] += B_C[i + 1]
    print(sum(A_B_C))

if __name__ == '__main__':
    main()