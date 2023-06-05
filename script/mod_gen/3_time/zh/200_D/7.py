def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    if N == 2:
        print('Yes')
        print('1 1')
        print('1 2')
        return
    # 用来存储所有可能的和
    s = set()
    # 用来存储和对应的下标
    d = dict()
    for i in range(N):
        for j in range(i+1, N):
            sum = A[i] + A[j]
            if sum % 200 in s:
                print('Yes')
                print('1', end=' ')
                print(d[sum % 200][0] + 1)
                print('1', end=' ')
                print(d[sum % 200][1] + 1)
                print(i + 1, j + 1)
                return
            else:
                s.add(sum % 200)
                d[sum % 200] = (i, j)
    print('No')

if __name__ == '__main__':
    main()