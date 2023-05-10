def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_orange = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(1, A[j]+1):
                if max_orange < sum(A[i:j+1]) - k*(j-i+1):
                    max_orange = sum(A[i:j+1]) - k*(j-i+1)
    print(max_orange)

if __name__ == '__main__':
    main()