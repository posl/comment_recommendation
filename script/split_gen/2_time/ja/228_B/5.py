def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    friends = [0]*N
    friends[X-1] = 1
    for i in range(N):
        if friends[A[X-1]] == 1:
            break
        friends[A[X-1]] = 1
        X = A[X-1]+1
    print(sum(friends))
