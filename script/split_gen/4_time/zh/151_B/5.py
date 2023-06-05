def main():
    # input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    # process
    score = N*M - sum(A)
    if score > K:
        score = -1
    elif score < 0:
        score = 0
    # output
    print(score)
