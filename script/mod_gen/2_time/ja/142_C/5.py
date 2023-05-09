def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    for i in range(N):
        if A[i] == N:
            print(i + 1, end = " ")
    for i in range(N):
        if A[i] != N:
            print(i + 1, end = " ")

if __name__ == '__main__':
    main()