def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1].add(d-1)
        blocks[d-1].add(c-1)
    for i in range(n):
        print(len(friends[i] - blocks[i] - {i}) - 1, end=' ')

if __name__ == '__main__':
    main()