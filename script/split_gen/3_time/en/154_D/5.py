def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    sum_p = [0]
    for i in range(1, N+1):
        sum_p.append(sum_p[i-1] + p[i])
    max_expect = 0
    for i in range(N-K+1):
        expect = (sum_p[i+K] - sum_p[i]) / 2 + p[i+K]
        if max_expect < expect:
            max_expect = expect
    print(max_expect)
