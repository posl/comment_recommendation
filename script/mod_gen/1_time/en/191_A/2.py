def main():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()