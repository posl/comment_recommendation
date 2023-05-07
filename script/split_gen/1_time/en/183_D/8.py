def main():
    N, W = map(int, input().split())
    T = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        T[S] += P
        T[T] -= P
    for i in range(1, 200001):
        T[i] += T[i - 1]
    print("Yes" if max(T) <= W else "No")
