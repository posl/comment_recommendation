def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        P_i, Y_i = map(int, input().split())
        P.append(P_i)
        Y.append(Y_i)
    #print(P)
    #print(Y)
    P_sorted = sorted(P)
    #print(P_sorted)
    P_sorted = sorted(P)
    #print(P_sorted)
    P_sorted_index = []
    for i in range(M):
        P_sorted_index.append(P_sorted.index(P[i]))
    #print(P_sorted_index)
    P_sorted_index_sorted = sorted(P_sorted_index)
    #print(P_sorted_index_sorted)
    P_sorted_index_sorted_index = []
    for i in range(M):
        P_sorted_index_sorted_index.append(P_sorted_index_sorted.index(P_sorted_index[i]))
    #print(P_sorted_index_sorted_index)
    for i in range(M):
        print("{0:06d}".format(P[i]) + "{0:06d}".format(P_sorted_index_sorted_index[i]+1))
    return
