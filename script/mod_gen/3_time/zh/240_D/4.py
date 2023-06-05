def main():
    N = input()
    A = raw_input().split()
    A = map(int, A)
    B = []
    for i in range(N):
        B.append(i)
    C = []
    for i in range(N):
        C.append(0)
    for i in range(N):
        C[A[i]-1] += 1
    for i in range(N):
        print N - sum(C[:A[i]-1]) - 1

if __name__ == '__main__':
    main()