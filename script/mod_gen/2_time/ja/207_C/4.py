def solve():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            L[i] = l
            R[i] = r
        elif t == 2:
            L[i] = l
            R[i] = r - 1
        elif t == 3:
            L[i] = l + 1
            R[i] = r
        else:
            L[i] = l + 1
            R[i] = r - 1
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] <= R[j] and L[j] <= R[i]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()