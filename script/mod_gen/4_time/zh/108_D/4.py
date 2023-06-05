def solve():
    L = int(input())
    N = 0
    M = 0
    #这里有个很重要的性质，就是当L为偶数时，构造的图中的边的长度可以为0~L-1之间的任意偶数，当L为奇数时，构造的图中的边的长度可以为0~L-1之间的任意奇数
    if L % 2 == 0:
        M = L
        N = L + 2
    else:
        M = L + 1
        N = L + 3
    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, i % 2)
    if L % 2 == 0:
        for i in range(1, L + 1):
            print(i, i + L // 2 + 1, i % 2)
    else:
        for i in range(1, L + 1):
            print(i, i + L // 2 + 2, i % 2)
    if L % 2 == 0:
        print(1, L + 3, L - 1)
        print(L + 2, L + 3, L - 1)
    else:
        print(1, L + 3, L)
        print(L + 2, L + 3, L - 2)

if __name__ == '__main__':
    solve()