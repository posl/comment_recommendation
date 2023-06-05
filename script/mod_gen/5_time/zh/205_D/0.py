def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        k = int(input())
        print(solve(n, a, k))

if __name__ == '__main__':
    main()