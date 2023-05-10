def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] == 1:
            for j in range(i+1, N):
                if (j+1) % (i+1) == 0:
                    A[j] = (A[j] + 1) % 2
    print(sum(A))
    for i in range(N):
        if A[i] == 1:
            print(i+1)

if __name__ == '__main__':
    main()