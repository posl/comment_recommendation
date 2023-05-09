def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    friend = [False] * (N + 1)
    count = 0
    while True:
        if friend[X] == True:
            break
        else:
            friend[X] = True
            count += 1
            X = A[X]
    print(count)
