def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T, A)
    time = 0
    for i in range(N):
        if T < time + A[i]:
            print(i + 1, T - time)
            break
        time += A[i]
        if i == N - 1:
            print(1, T - time)
