def main():
    N, Q = map(int, input().split())
    S = input()
    A = [0] * N
    for i in range(1, N):
        if S[i-1:i+1] == "AC":
            A[i] = A[i-1] + 1
        else:
            A[i] = A[i-1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(A[r-1] - A[l-1])
main()

if __name__ == '__main__':
    main()