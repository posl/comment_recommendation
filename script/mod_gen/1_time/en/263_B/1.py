def main():
    n = int(input())
    p = list(map(int, input().split()))
    parent = [0] * n
    for i in range(1, n):
        parent[p[i - 1] - 1] += 1
    print(max(parent))

if __name__ == '__main__':
    main()