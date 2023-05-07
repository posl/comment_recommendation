def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    ans = K
    for A, B in friends:
        if ans >= A:
            ans += B
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()