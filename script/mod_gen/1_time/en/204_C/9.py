def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 0-index
    AB = [[a - 1, b - 1] for a, b in AB]
    # count the number of cities that can be reached from city i
    # (directly or indirectly)
    reach = [0] * N
    for a, b in AB:
        reach[a] += 1
        reach[b] += 1
    # count the number of pairs (a, b) where a can reach b
    reach_to = [0] * N
    for a, b in AB:
        if reach[a] < reach[b]:
            reach_to[a] += 1
        else:
            reach_to[b] += 1
    ans = sum(r * (r - 1) for r in reach_to)
    print(ans)

if __name__ == '__main__':
    main()