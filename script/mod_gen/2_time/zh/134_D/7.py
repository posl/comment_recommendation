def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max_A = max(A)
    for i in range(N):
        if A[i] == max_A:
            print(max(A[:i] + A[i+1:]))
        else:
            print(max_A)

if __name__ == '__main__':
    main()