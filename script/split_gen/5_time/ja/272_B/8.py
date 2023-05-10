def main():
    N, M = map(int, input().split())
    X = []
    for i in range(M):
        X.append(list(map(int, input().split()))[1:])
    for i in range(M):
        for j in range(i+1, M):
            if len(set(X[i]) & set(X[j])) != 0:
                print("Yes")
                return
    print("No")
