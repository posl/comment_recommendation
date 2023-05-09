def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    if N == 0:
        print(X)
    else:
        i = 0
        while i < N:
            if X - p[i] < 0:
                break
            i += 1
        if i == 0:
            print(p[0])
        elif i == N:
            print(p[N-1])
        else:
            if p[i] - X < X - p[i-1]:
                print(p[i])
            elif p[i] - X > X - p[i-1]:
                print(p[i-1])
            else:
                print(p[i-1])
