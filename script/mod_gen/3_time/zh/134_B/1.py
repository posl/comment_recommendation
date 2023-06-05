def solution(N, D):
    if N == 1:
        return 1
    if D == 1:
        return N
    count = 0
    while N > 0:
        count += 1
        N = N - (2 * D + 1)
    return count

if __name__ == '__main__':
    solution()