def main():
    N, M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if set(x[i]) & set(x[j]):
                print("Yes")
                return
    print("No")
