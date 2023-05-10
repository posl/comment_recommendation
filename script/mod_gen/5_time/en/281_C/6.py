def problem281_c():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = 0
    for i in range(N):
        if time + A[i] > T:
            print(i+1, T - time)
            return
        time += A[i]
    print((T//time)*N + 1, T - (T//time)*time)

if __name__ == '__main__':
    problem281_c()