def main():
    N, Q = map(int, input().split())
    train = [0] * (N + 1)
    for i in range(1, N+1):
        train[i] = i
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[2]] = train[query[1]]
        if query[0] == 2:
            train[query[2]] = query[2]
        if query[0] == 3:
            ans = []
            for j in range(1, N+1):
                if train[j] == train[query[1]]:
                    ans.append(j)
            print(len(ans), *ans)
