def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    t = T % S
    for i in range(N):
        if t - A[i] < 0:
            print(i+1, t)
            break
        t -= A[i]
