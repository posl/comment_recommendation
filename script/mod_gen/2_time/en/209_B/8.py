def main():
    #input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #output
    print('Yes' if sum([A[i] - i % 2 for i in range(N)]) <= X else 'No')

if __name__ == '__main__':
    main()