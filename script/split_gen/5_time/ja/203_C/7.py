def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    #print(AB)
    for i in range(N):
        if AB[i][0] > K:
            print(K)
            break
        else:
            K += AB[i][1]
    else:
        print(K)
