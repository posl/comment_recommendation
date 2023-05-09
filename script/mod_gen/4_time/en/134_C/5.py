def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for i in range(N):
        if A[i] == maxA:
            print(max(A[:i] + A[i+1:]))
        else:
            print(maxA)

if __name__ == '__main__':
    main()