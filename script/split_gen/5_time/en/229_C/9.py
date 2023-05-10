def max_deliciousness(N, W, A, B):
    #print("N: ", N, "W: ", W, "A: ", A, "B:", B)
    #print("max(A): ", max(A), "max(B): ", max(B))
    #print("sum(B): ", sum(B))
    #print("sum(A): ", sum(A))
    #print("W: ", W)
    if sum(B) <= W:
        return sum(A)
    else:
        max_del = 0
        for i in range(N):
            max_del += (A[i] * min(B[i], W))
            W -= min(B[i], W)
            if W == 0:
                break
        return max_del
