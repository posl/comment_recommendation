def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    max_dist = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5
            max_dist = max(max_dist, dist)
    print(max_dist)
