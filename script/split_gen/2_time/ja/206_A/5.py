def main():
    N = int(input())
    ans = N * 1.08
    if ans < 206:
        print('Yay!')
    elif ans > 206:
        print(':(')
    else:
        print('so-so')
