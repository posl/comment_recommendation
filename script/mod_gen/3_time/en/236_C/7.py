def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    # Express trains may stop at all stations.
    if n == m:
        print('Yes' * n)
        return
    # Express trains may stop at only M (M ≦ N) stations.
    # T_1 = S_1 and T_M = S_N.
    # (T_1, ..., T_M) is obtained by removing zero or more strings from (S_1, ..., S_N) and lining up the remaining strings without changing the order.
    i = 0
    j = 0
    while i < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
        if j == m:
            break
    if j == m:
        print('Yes' * (i - m) + 'No' * (n - i + m) + 'Yes' * m)
    else:
        print('No' * n)

if __name__ == '__main__':
    main()