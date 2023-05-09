def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    A.remove(maxA)
    maxA2 = max(A)
    for i in range(N):
        if A[i] == maxA:
            print(maxA2)
        else:
            print(maxA)

if __name__ == '__main__':
    main()