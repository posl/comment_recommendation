def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
    print(ans)
