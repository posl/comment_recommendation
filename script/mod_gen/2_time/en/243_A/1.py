def main():
    V, A, B, C = map(int, input().split())
    if A >= V:
        print('F')
    elif A + B >= V:
        print('M')
    else:
        print('T')

if __name__ == '__main__':
    main()