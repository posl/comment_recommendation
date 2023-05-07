def main():
    N, M = map(int, input().split())
    X = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        if a + 1 == b:
            X[a] += 1
        elif b + 1 == a:
            X[b] += 1
        else:
            print("No")
            exit()
    if sum(X) == M:
        print("Yes")
    else:
        print("No")
