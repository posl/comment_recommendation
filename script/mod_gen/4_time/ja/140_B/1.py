def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i > 0 and A[i] - A[i - 1] == 1:
            satisfaction += C[A[i - 1] - 1]
    print(satisfaction)

if __name__ == '__main__':
    main()