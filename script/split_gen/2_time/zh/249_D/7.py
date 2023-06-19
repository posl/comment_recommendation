def solve(N, A):
    dic = {}
    for i in range(N):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0:
                if A[i] // A[j] in dic:
                    ans += dic[A[i] // A[j]]
    return ans
