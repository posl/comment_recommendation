def teleporter():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    count = 0
    while count < K:
        town = A[town-1]
        count += 1
    print(town)
