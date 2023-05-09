def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        A, B = map(int, input().split())
        edges.append((A, B))
    K = int(input())
    people = []
    for _ in range(K):
        C, D = map(int, input().split())
        people.append((C, D))
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if (i>>j)&1:
                balls[people[j][0]] += 1
            else:
                balls[people[j][1]] += 1
        tmp = 0
        for A, B in edges:
            if balls[A] > 0 and balls[B] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()