def subseq_sum(A, K):
    N = len(A)
    s = [0]
    for i in range(N):
        s.append(s[-1]+A[i])
    #print(s)
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[s[i]] += 1
    #print(d)
    ans = 0
    for i in range(N+1):
        ans += d[s[i]-K]
    return ans

if __name__ == '__main__':
    subseq_sum()