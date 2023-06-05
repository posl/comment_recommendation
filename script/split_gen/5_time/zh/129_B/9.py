def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    T = 100000
    for i in range(N):
        T = min(T, abs(S - 2 * sum(W[:i+1])))
    print(T)
