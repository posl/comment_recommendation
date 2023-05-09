def friends_learn_the_secret():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 1
    for i in range(1, N):
        if A[X] == 0:
            return count
        else:
            X = A[X]
            count += 1
    return count
