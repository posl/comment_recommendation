def main():
    # input
    n = int(input())
    # process
    n = int(n * 1.08)
    if n < 206:
        print('Yay!')
    elif n == 206:
        print('so-so')
    else:
        print(':(')
