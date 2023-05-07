def get_num_of_sequences(a, b):
    def get_num_of_sequences_sub(a, b, a_idx, b_idx, dp):
        if a_idx == len(a):
            return 1
        if dp[a_idx][b_idx] != -1:
            return dp[a_idx][b_idx]
        res = 0
        for i in range(b_idx, len(b)):
            if a[a_idx] <= b[i]:
                res += get_num_of_sequences_sub(a, b, a_idx + 1, i, dp)
        dp[a_idx][b_idx] = res
        return res
    dp = [[-1 for _ in range(len(b))] for _ in range(len(a))]
    return get_num_of_sequences_sub(a, b, 0, 0, dp)

if __name__ == '__main__':
    get_num_of_sequences()