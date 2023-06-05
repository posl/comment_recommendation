def main():
    #input
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split()))[1:])
    #calc
    Snuke = [0 for i in range(N)]
    for i in range(K):
        for j in range(len(A[i])):
            Snuke[A[i][j]-1] += 1
    #output
    count = 0
    for i in range(N):
        if Snuke[i] == 0:
            count += 1
    print(count)
