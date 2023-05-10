def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**30
    for i in range(2**(N-1)):
        tmp = 0
        tmp2 = 0
        for j in range(N):
            tmp = tmp | A[j]
            if i >> j & 1:
                tmp2 = tmp2 ^ tmp
                tmp = 0
        tmp2 = tmp2 ^ tmp
        ans = min(ans, tmp2)
    print(ans)
