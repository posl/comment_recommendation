def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    counter = [0] * (N+1)
    for a in A:
        counter[a] += 1
    for l, r, x in queries:
        print(counter[x])

if __name__ == '__main__':
    main()