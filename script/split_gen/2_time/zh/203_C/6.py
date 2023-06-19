def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort()
    for friend in friends:
        if friend[0] <= K:
            K += friend[1]
        else:
            break
    print(K)
