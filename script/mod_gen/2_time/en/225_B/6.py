def main():
    N = int(input())
    nodes = [0] * N
    for _ in range(N - 1):
        a, b = map(int, input().split())
        nodes[a - 1] += 1
        nodes[b - 1] += 1
    print('Yes' if max(nodes) == N - 1 else 'No')

if __name__ == '__main__':
    main()