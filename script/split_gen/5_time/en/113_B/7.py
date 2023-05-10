def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 100000000000000
    min_diff_i = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_i = i
    print(min_diff_i + 1)
