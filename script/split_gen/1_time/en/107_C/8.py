def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    time = 10**9
    for i in range(N-K+1):
        if x[i+K-1] < 0:
            t = abs(x[i])
        elif x[i] > 0:
            t = x[i+K-1]
        else:
            t = 2*x[i+K-1] + abs(x[i])
        if t < time:
            time = t
    print(time)
