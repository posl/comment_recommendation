def get_day(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            return i
