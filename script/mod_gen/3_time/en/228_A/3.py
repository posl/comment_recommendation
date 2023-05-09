def main():
    S, T, X = map(int, input().split())
    if S <= X < T:
        print('Yes')
    elif S > T and (X < T or S <= X):
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()