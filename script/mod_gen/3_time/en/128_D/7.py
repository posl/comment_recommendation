def max_sum(N, K, V):
    result = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            left = V[:j]
            right = V[N-(i-j):]
            left.sort()
            right.sort()
            for k in range(min(K-i, j)):
                if left[k] < 0:
                    left[k] = 0
            for k in range(min(K-i, i-j)):
                if right[k] < 0:
                    right[k] = 0
            result = max(result, sum(left)+sum(right))
    return result

if __name__ == '__main__':
    max_sum()