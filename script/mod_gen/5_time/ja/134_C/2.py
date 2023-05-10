def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    B = sorted(A)
    for i in range(N):
        if A[i] == B[-1]:
            print(B[-2])
        else:
            print(B[-1])

if __name__ == '__main__':
    main()