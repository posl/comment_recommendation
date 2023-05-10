def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        if A[i] == max(A):
            print(max(A[:i]+A[i+1:]))
        else:
            print(max(A))

if __name__ == '__main__':
    main()