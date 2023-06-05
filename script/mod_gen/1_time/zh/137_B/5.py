def main():
    K, X = [int(x) for x in input().split()]
    print(' '.join([str(x) for x in range(X-K+1, X+K)]))

if __name__ == '__main__':
    main()