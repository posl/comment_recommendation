def get_last_card(n,k,a):
    # n,k,a = input().split()
    # n = int(n)
    # k = int(k)
    # a = int(a)
    n = int(n)
    k = int(k)
    a = int(a)
    if n == 1:
        return 1
    if a+k <= n:
        return a+k
    else:
        return a+k-n

if __name__ == '__main__':
    get_last_card()