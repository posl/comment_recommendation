def change(N):
    change = 1000 - N%1000
    if change == 1000:
        return 0
    else:
        return change

if __name__ == '__main__':
    change()