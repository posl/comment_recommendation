def main():
    n, m, k = map(int, input().split())
    friends = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1] += 1
        friends[b-1] += 1
    blocks = [0] * n
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1] += 1
        blocks[d-1] += 1
    for i in range(n):
        print(friends[i] - blocks[i] - 1)
