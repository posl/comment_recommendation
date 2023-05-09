def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    diff = 100000000
    for i in range(1, N):
        diff = min(diff, abs(sum(W[:i]) - sum(W[i:])))
    print(diff)

if __name__ == '__main__':
    main()