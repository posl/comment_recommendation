def solve():
    n, k = map(int, input().split())
    friends = []
    for _ in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort()
    v = 0
    for a, b in friends:
        if a > v + k:
            break
        k -= a - v
        v = a
        k += b
    v += k
    print(v)

if __name__ == '__main__':
    solve()