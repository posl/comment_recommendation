def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max = max(A)
    for i in range(N):
        if A[i] == max:
            print(max(A[0:i]+A[i+1:N]))
        else:
            print(max)

if __name__ == '__main__':
    main()