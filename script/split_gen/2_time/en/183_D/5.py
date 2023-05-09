def main():
    N, W = map(int, input().split())
    diff = [0] * 200002
    for i in range(N):
        S, T, P = map(int, input().split())
        diff[S] += P
        diff[T] -= P
    for i in range(1, 200002):
        diff[i] += diff[i - 1]
    if max(diff) <= W:
        print('Yes')
    else:
        print('No')
