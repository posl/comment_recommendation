def main():
    n, m, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    cd = [list(map(int, input().split())) for _ in range(k)]
    friend = [0] * (n + 1)
    block = [0] * (n + 1)
    for a, b in ab:
        friend[a] += 1
        friend[b] += 1
    for c, d in cd:
        block[c] += 1
        block[d] += 1
    for i in range(1, n + 1):
        print(friend[i] - block[i] - 1, end=" ")

if __name__ == '__main__':
    main()