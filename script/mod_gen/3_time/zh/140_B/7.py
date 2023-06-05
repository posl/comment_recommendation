def main():
    N = int(input())
    A = input().split()
    B = input().split()
    C = input().split()
    satisfaction = 0
    for i in range(N):
        satisfaction += int(B[i])
        if i < N-1 and int(A[i+1]) == int(A[i]) + 1:
            satisfaction += int(C[i])
    print(satisfaction)

if __name__ == '__main__':
    main()