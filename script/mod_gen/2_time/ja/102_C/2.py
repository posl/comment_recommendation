def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    b = A[N//2]
    print(sum(abs(b - a) for a in A))

if __name__ == '__main__':
    main()