def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        cnt += B.count(C[A[i]-1])
    print(cnt)

if __name__ == '__main__':
    main()