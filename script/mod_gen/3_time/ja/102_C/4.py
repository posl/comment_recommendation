def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [i+1 for i in range(N)]
    C = [abs(A[i]-B[i]) for i in range(N)]
    print(sum(C))

if __name__ == '__main__':
    main()