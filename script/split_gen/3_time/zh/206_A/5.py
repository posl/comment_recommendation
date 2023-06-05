def main():
    n = int(input())
    p = int(n * 1.08)
    if p < 206:
        print('Yay!')
    elif p == 206:
        print('so-so')
    else:
        print(':(')
