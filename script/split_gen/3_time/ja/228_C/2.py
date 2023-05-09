def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: sum(x), reverse=True)
    #print(P)
    for i in range(N):
        if i < K-1:
            print("Yes")
        else:
            if sum(P[i]) < sum(P[K-1]):
                print("No")
            else:
                print("Yes")
