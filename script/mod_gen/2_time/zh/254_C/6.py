def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    if K == 1:
        print('Yes')
        return
    for i in range(N-K):
        if a[i] > a[i+K]:
            print('No')
            return
    print('Yes')
    return
main()
