def main():
    S = input()
    S = S[::-1]
    S = 'a' + S
    print('Yes' if S == S[::-1] else 'No')

if __name__ == '__main__':
    main()