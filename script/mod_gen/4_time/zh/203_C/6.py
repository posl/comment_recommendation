def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append([a, b])
    friends.sort()
    last = 0
    for i in range(n):
        if friends[i][0] - last <= k:
            k -= friends[i][0] - last
            k += friends[i][1]
            last = friends[i][0]
        else:
            print(last + k)
            return
    print(last + k)

if __name__ == '__main__':
    main()