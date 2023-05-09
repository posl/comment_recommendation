def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    for ki in k:
        print(solve(n, a, ki))

if __name__ == '__main__':
    main()