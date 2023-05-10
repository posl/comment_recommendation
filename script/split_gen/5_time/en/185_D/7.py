def min_stamp(N, M, A):
    if M == 0:
        return 1
    A.sort()
    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)
    diff = []
    for i in range(len(A)-1):
        diff.append(A[i+1]-A[i]-1)
    diff = [x for x in diff if x != 0]
    if len(diff) == 0:
        return 0
    return min(diff)
