def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = 0
    count = 0
    for i in range(N):
        if time + A[i] > T:
            break
        time += A[i]
        count += 1
    print(count + 1, T - time)
