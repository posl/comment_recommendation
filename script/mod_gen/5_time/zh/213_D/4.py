def main():
    N = int(input())
    cities = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        cities[a-1].append(b)
        cities[b-1].append(a)
    for i in range(N):
        cities[i].sort()
    ans = []
    stack = [1]
    while len(stack) > 0:
        current = stack.pop()
        ans.append(current)
        for i in range(len(cities[current-1])-1, -1, -1):
            next = cities[current-1][i]
            cities[next-1].remove(current)
            stack.append(next)
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()