def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    A_max = A[-1]
    A_max_2 = A[-2]
    for i in range(N):
        if A[i] == A_max:
            print(A_max_2)
        else:
            print(A_max)
    return

if __name__ == '__main__':
    main()