def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2 ** 30
    for i in range(2 ** (N - 1)):
        bits = bin(i)[2:].zfill(N - 1)
        res = 0
        tmp = A[0]
        for j in range(N - 1):
            if bits[j] == '1':
                res ^= tmp
                tmp = A[j + 1]
            else:
                tmp |= A[j + 1]
        res ^= tmp
        ans = min(ans, res)
    print(ans)
