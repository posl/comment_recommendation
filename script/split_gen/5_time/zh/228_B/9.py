def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    friends = [False] * N
    friends[X - 1] = True
    count = 1
    while True:
        if friends[A[X - 1]]:
            break
        friends[A[X - 1]] = True
        count += 1
        X = A[X - 1] + 1
    print(count)
