def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    ans = [0] * N
    for i in range(N-1):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans[cnt] += 1
            cnt = 0
    ans[cnt] += 1
    for i in range(N):
        print(ans[i])
