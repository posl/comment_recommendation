def max_sum(N,K,V):
    if K >= N:
        return sum(V)
    else:
        max_sum = 0
        for i in range(K+1):
            for j in range(i+1):
                sum_left = sum(V[:j])
                sum_right = sum(V[N-(i-j):])
                if sum_left + sum_right > max_sum:
                    max_sum = sum_left + sum_right
        return max_sum

if __name__ == '__main__':
    max_sum()