def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X and X < T:
            print('Yes')
        else:
            print('No')
    elif S > T:
        if S <= X or X < T:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()