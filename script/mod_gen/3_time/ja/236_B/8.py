def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N):
        print(A[4*i+1])

if __name__ == '__main__':
    main()