Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][1] = 1
    for i in range(N):
        if S[i] == "AND":
            dp[i+1][0] = dp[i][0]*2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]*2 + dp[i][0]
    print(dp[N][1])

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if S[-1] == "AND":
        print(2 ** (N + 1) - 2 ** N)
    else:
        print(2 ** (N + 1))

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == "AND":
            ans *= 2
        else:
            ans = ans*2+1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # y_0 = x_0
    # i >= 1 のとき、S_i が AND なら y_i=y_{i-1} ∧ x_i、S_i が OR なら y_i=y_{i-1} ∨ x_i
    # a ∧ b は a と b の論理積を表し、a ∨ b は a と b の論理和を表します。
    # a と b の論理積は、a と b のどちらかが False なら False で、両方が True なら True です。
    # a と b の論理和は、a と b のどちらかが True なら True で、両方が False なら False です。
    # y_0 = x_0 なので、y_0 は True か False です。
    # y_0 が True のとき、y_1 は x_1 によらず True です。
    # y_0 が False のとき、y_1 は x_1 によらず False です。
    # y_1 が True のとき、y_2 は x_2 によらず True です。
    # y_1 が False のとき、y_2 は x_2 によらず False です。
    # ...
    # y_{N-1} が True のとき、y_N は x_N によらず True です。
    # y_{N-1} が False のとき、y_N は x_N によらず False です。
    # y_N が True のとき、y_N は x_N によらず True です。
    # y_N が False のとき、y_N は x_N によらず False です。
    # つまり、y_i は x_i によらず True または

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        y = i % 2
        for j in range(n):
            x = (i >> j) % 2
            if s[j] == 'AND':
                y = y & x
            else:
                y = y | x
        if y == 1:
            ans += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 2**(N-1)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    ans = 2 ** (N - 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    count = 0
    for i in range(2**N):
        x = list(format(i, '0' + str(N) + 'b'))
        x = [True if x[i] == '1' else False for i in range(N)]
        y = [x[0]]
        for i in range(1, N):
            if S[i] == 'AND':
                y.append(y[i-1] and x[i])
            else:
                y.append(y[i-1] or x[i])
        if y[-1] == True:
            count += 1
    print(count)
