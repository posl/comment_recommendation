def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    ans = 10**9
    for i in range(101):
        cnt = 0
        for j in range(H):
            for k in range(W):
                if A[j][k] > i:
                    cnt += A[j][k] - i
        ans = min(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()