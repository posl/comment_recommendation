def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = i - A[:i].count(A[i])
    for a in ans:
        print(a)
