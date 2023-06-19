def main():
    n,m = map(int,input().split())
    if n == 1:
        print('Yes')
        return
    if m == 0:
        print('No')
        return
    # 有m条边，n个点，m>=n-1
    if m < n-1:
        print('No')
        return
    # 有m条边，n个点，m<=n(n-1)/2
    if m > n*(n-1)/2:
        print('No')
        return
    # 有m条边，n个点，m>=n-1, m<=n(n-1)/2
    print('Yes')
