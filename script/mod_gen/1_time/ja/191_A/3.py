def main():
    V, T, S, D = map(int, input().split())
    if D < V * T or V * S < D:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()