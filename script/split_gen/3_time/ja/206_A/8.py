def main():
    N = int(input())
    if N * 1.08 < 206:
        print('Yay!')
    elif N * 1.08 > 206:
        print(':(')
    else:
        print('so-so')
