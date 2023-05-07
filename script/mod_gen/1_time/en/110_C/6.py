def main():
    S = input()
    T = input()
    S = sorted(S)
    T = sorted(T, reverse=True)
    print('Yes' if S < T else 'No')

if __name__ == '__main__':
    main()