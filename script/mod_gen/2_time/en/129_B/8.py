def main():
    N = int(input())
    W = list(map(int, input().split()))
    W_ = []
    for i in range(1, N):
        W_ += [abs(sum(W[:i]) - sum(W[i:]))]
    print(min(W_))

if __name__ == '__main__':
    main()