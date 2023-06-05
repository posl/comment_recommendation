def problems129_b():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000000000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    problems129_b()