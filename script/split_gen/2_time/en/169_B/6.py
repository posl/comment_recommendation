def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    flag = 0
    for i in range(N):
        if A[i] == 0:
            flag = 1
            print(0)
            break
        if ans > 10 ** 18 // A[i]:
            flag = 1
            print(-1)
            break
        ans *= A[i]
    if flag == 0:
        print(ans)
