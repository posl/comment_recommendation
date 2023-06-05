def max_sum(N, K, V):
    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            left = V[:i]
            right = V[N-j:]
            left.sort()
            right.sort()
            ans = max(ans, sum(right)-sum(left))
    return ans

if __name__ == '__main__':
    max_sum()