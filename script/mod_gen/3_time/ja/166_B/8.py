def main():
    N, K = map(int, input().split())
    #A = []
    A = [0]*N
    for i in range(K):
        d = int(input())
        A_ = list(map(int,input().split()))
        for j in range(d):
            A[A_[j]-1] += 1
    ans = 0
    for i in range(N):
        if A[i] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()