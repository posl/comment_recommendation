def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i]-(i+1) for i in range(N)]
    A.sort()
    b = A[N//2]
    print(sum([abs(A[i]-b) for i in range(N)]))

if __name__ == '__main__':
    main()