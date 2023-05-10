def main():
    N, Q = map(int, input().split())
    train = [[] for _ in range(N)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1].append(query[2])
            train[query[2]-1].append(query[1])
        elif query[0] == 2:
            train[query[1]-1].remove(query[2])
            train[query[2]-1].remove(query[1])
        else:
            print(*train[query[1]-1])
