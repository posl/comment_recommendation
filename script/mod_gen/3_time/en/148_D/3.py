def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a - 1] += 1
    for b in B:
        if b > 1:
            print(-1)
            return
    if B[0] == 0:
        print(-1)
        return
    ans = 0
    cnt = 0
    for a in A:
        if a == 1:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(N - ans)

if __name__ == '__main__':
    main()