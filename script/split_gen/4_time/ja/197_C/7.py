def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**31-1
    for i in range(2**(N-1)):
        or_list = []
        xor_list = []
        tmp = 0
        for j in range(N):
            tmp |= A[j]
            if (i >> j) & 1:
                xor_list.append(tmp)
                tmp = 0
        xor_list.append(tmp)
        for xor in xor_list:
            ans = min(ans, xor)
    print(ans)
main()
