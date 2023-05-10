def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        print(max(A[:i]+A[i+1:]))

if __name__ == '__main__':
    main()