def main():
    S = [input() for _ in range(4)]
    S.sort()
    if S == ['2B', '3B', 'H', 'HR']:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()