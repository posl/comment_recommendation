def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(X)
    friends = [0] * N
    friends[X - 1] = 1
    for i in range(N):
        if friends[i] == 1:
            friends[A[i] - 1] = 1
    print(sum(friends))
main()
