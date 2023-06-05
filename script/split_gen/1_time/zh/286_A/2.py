def swap_list(list, p, q, r, s):
    list[p-1:q],list[r-1:s] = list[r-1:s],list[p-1:q]
    return list
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap_list(A, P, Q, R, S)
print(' '.join(str(i) for i in B))
