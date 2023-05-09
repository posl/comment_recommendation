def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    A_sorted_set = set(A_sorted)
    A_sorted_dict = {}
    for i, a in enumerate(A_sorted_set):
        A_sorted_dict[a] = i
    A_sorted_dict_rev = {}
    for k, v in A_sorted_dict.items():
        A_sorted_dict_rev[v] = k
    A_sorted_dict_rev_sorted = sorted(A_sorted_dict_rev.items(), key=lambda x:x[0])
    A_sorted_dict_rev_sorted_dict = {}
    for i, (k, v) in enumerate(A_sorted_dict_rev_sorted):
        A_sorted_dict_rev_sorted_dict[k] = v
    for i in range(N):
        print(K//N, flush=True)
        if K//N > 0:
            K -= K//N
        else:
            K = 0
        if K == 0:
            break
    if K == 0:
        return
    for i in range(K):
        print(A_sorted_dict_rev_sorted_dict[i]+1, flush=True)

if __name__ == '__main__':
    main()