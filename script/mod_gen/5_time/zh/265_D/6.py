def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    P -= 1
    Q -= 1
    R -= 1
    A.sort()
    ans = 0
    for i in range(N):
        if i > 0 and A[i] == A[i - 1]:
            continue
        if A[i] > R:
            break
        x = i
        y = -1
        z = -1
        for j in range(i + 1, N):
            if j > i + 1 and A[j] == A[j - 1]:
                continue
            if A[j] > Q:
                break
            if A[j] == A[i]:
                y = j
            else:
                z = j
        if y == -1 or z == -1:
            continue
        for j in range(z + 1, N):
            if j > z + 1 and A[j] == A[j - 1]:
                continue
            if A[j] > P:
                break
            if A[j] == A[z]:
                ans += 1
                break
    if ans > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()