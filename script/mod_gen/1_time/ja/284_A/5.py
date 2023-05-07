def main():
    N = int(input())
    S = [input() for i in range(N)]
    print('
'.join(S[::-1]))

if __name__ == '__main__':
    main()