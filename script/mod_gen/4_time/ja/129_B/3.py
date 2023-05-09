def problems129_b():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff
print(problems129_b())

if __name__ == '__main__':
    problems129_b()