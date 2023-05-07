def main():
    N = int(input())
    tax = N * 1.08
    if tax > 206:
        print(':(')
    elif tax < 206:
        print('Yay!')
    else:
        print('so-so')
