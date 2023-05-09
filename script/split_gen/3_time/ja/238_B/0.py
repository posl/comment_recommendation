def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i == j:
                continue
            if A[i] > A[j]:
                tmp += A[i] - A[j]
            else:
                tmp += A[j] - A[i]
        if ans < tmp:
            ans = tmp
    print(ans)
