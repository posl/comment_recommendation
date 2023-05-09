def main():
    S, T, X = map(int, input().split())
    if (S <= X and X < T) or (S <= X + 24 and X + 24 < T):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()