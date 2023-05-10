def main():
    N = int(input())
    A = list(map(int, input().split()))
    ret = 2**30
    for i in range(2**(N-1)):
        tmp = 0
        xor = 0
        for j in range(N):
            tmp |= A[j]
            if i & (1 << j):
                xor ^= tmp
                tmp = 0
        xor ^= tmp
        ret = min(ret, xor)
    print(ret)

if __name__ == '__main__':
    main()