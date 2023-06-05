def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T - 1
    T = T % sum(A)
    for i in range(N):
        T = T - A[i]
        if T < 0:
            print(i + 1, -T)
            break
