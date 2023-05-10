def main():
    N, W = map(int, input().split())
    s = [0] * (200001)
    for i in range(N):
        S, T, P = map(int, input().split())
        s[S] += P
        s[T] -= P
    for i in range(1, 200001):
        s[i] += s[i-1]
        if s[i] > W:
            print("No")
            return
    print("Yes")
