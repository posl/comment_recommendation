def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    if K == 1:
        for i in range(N-1):
            if a[i] > a[i+1]:
                print('No')
                return
        print('Yes')
        return
    for i in range(N-K):
        if a[i] > a[i+K]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    solve()