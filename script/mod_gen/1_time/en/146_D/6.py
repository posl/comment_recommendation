def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    print(n-1)
    for a, b in edges:
        print(min(a, b))

if __name__ == '__main__':
    main()