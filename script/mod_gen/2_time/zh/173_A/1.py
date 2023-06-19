def change(N):
    if N % 1000 == 0:
        return 0
    else:
        return 1000 - N % 1000

if __name__ == '__main__':
    change()