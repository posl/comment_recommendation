Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += dpsum[max(0, i - l)] - dpsum[max(0, i - r - 1)]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])
solve()

=======
Suggestion 3

def check_list(list):
    for i in range(0,len(list)):
        if list[i] == 0:
            return False
    return True

=======
Suggestion 4

def problems179_d():
    pass

=======
Suggestion 5

def main():
    print("Hello world!")

=======
Suggestion 6

def get_input():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    return N, K, LRs

=======
Suggestion 7

def input():
    input_str = input()
    input_list = input_str.split(' ')
    N = int(input_list[0])
    K = int(input_list[1])
    L = []
    R = []
    for i in range(K):
        input_str = input()
        input_list = input_str.split(' ')
        L.append(int(input_list[0]))
        R.append(int(input_list[1]))
    return N, K, L, R
