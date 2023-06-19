def get_first_time(N, S, T):
    time = [0] * N
    for i in range(N):
        time[i] = T[i]
    for i in range(N):
        if (i == 0):
            if (S[i] > T[i]):
                time[i] = S[i]
        else:
            if (S[i] > T[i - 1] + S[i - 1]):
                time[i] = S[i]
            else:
                time[i] = T[i - 1] + S[i - 1] + S[i]
    return time

if __name__ == '__main__':
    get_first_time()