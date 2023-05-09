def main():
    S,T,X = [int(x) for x in input().split()]
    if S <= X and X < T:
        print('Yes')
    elif S > T and (X >= S or X < T):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()