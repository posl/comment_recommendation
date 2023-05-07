def sunny_or_rainy():
    N = int(input())
    S = input()
    if S[N-1] == 'o':
        print('Yes')
    else:
        print('No')
sunny_or_rainy()

if __name__ == '__main__':
    sunny_or_rainy()