def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i]-i-1 for i in range(N)]
    B.sort()
    b = B[N//2]
    print(sum(abs(B[i]-b) for i in range(N)))

if __name__ == '__main__':
    main()