def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K-Q for _ in range(N)]
    for a in A:
        ans[a-1] += 1
    for a in ans:
        if a > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()