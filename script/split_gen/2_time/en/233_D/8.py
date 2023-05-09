def solve(N,K,A):
    # write your code in Python 3.6
    sum = 0
    count = 0
    dic = {}
    dic[0] = 1
    for i in range(N):
        sum += A[i]
        if sum - K in dic:
            count += dic[sum - K]
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1
    return count
