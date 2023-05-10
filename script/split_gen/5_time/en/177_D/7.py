def main():
    N, M = map(int, input().split())
    friends = []
    for _ in range(M):
        A, B = map(int, input().split())
        friends.append([A, B])
    print(len(set([i for i in range(1, N+1)]) - set([i for i, j in friends if i in j or j in i])))
