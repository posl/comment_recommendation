def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(x % 200, i) for i, x in enumerate(A)]
    A.sort()
    for i in range(N-1):
        if A[i][0] == A[i+1][0]:
            print("Yes")
            print(i+1, A[i][1]+1, A[i+1][1]+1)
            print(N-i-1, A[i+2][1]+1, A[i+3][1]+1)
            return
    print("No")

if __name__ == '__main__':
    main()