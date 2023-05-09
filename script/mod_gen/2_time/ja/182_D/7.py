def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = [A[i] + A[i - 1] for i in range(1, N + 1)]
    print(max(A) - min(A))

if __name__ == '__main__':
    main()