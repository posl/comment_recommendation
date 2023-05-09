def find_song(N, T, A):
    total = 0
    for i in range(N):
        total += A[i]
        if total >= T:
            return i + 1, T - (total - A[i])

if __name__ == '__main__':
    find_song()