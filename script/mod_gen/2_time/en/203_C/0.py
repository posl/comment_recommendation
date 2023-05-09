def solve():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    money = K
    village = 0
    for A, B in friends:
        if A <= village:
            money += B
        else:
            break
    village += money
    print(village)

if __name__ == '__main__':
    solve()