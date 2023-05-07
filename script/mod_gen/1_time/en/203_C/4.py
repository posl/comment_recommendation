def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    pos = 0
    for A, B in friends:
        if A - pos > K:
            break
        K -= A - pos
        K += B
        pos = A
    pos += K
    print(pos)

if __name__ == '__main__':
    main()