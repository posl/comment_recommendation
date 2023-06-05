def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    if L < 0 and R < 0:
        for i in range(N):
            if A[i] < 0:
                ans += -L * A[i]
            else:
                ans += -R * A[i]
    elif L < 0 and R >= 0:
        for i in range(N):
            if A[i] < 0:
                ans += -L * A[i]
            else:
                ans += R * A[i]
    elif L >= 0 and R < 0:
        for i in range(N):
            if A[i] < 0:
                ans += L * A[i]
            else:
                ans += -R * A[i]
    else:
        for i in range(N):
            if A[i] < 0:
                ans += L * A[i]
            else:
                ans += R * A[i]
    print(ans)
