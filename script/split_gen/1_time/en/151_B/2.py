def main():
    N, K, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    score = M * N - sum(A)
    if score <= 0:
        print(0)
    elif score > K:
        print(-1)
    else:
        print(score)
