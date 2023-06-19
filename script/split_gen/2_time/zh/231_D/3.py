def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B-1)
        edge[B-1].append(A-1)
    #print(edge)
    #print(len(edge[0]))
    #print(len(edge[1]))
    #print(len(edge[2]))
    #print(len(edge[3]))
    for i in range(N):
        if len(edge[i]) % 2 == 1:
            print("No")
            return
    print("Yes")
