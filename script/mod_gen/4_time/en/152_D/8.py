def count(N):
    if N < 10:
        return N
    else:
        return 9 + count(N-1)

if __name__ == '__main__':
    count()