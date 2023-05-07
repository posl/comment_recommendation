def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    s = 0
    for i in range(N):
        s += A[i]
        if s > T:
            print(i)
            break
    else:
        print(N)
