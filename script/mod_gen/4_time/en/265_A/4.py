def buy_apple(X, Y, N):
    if N % 3 == 0:
        return int(N / 3) * Y
    else:
        return int(N / 3) * Y + (N % 3) * X

if __name__ == '__main__':
    buy_apple()