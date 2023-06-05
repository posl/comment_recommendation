def main():
    N,C = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    C = [AB[i][2] for i in range(N)]
    total = 0
    for i in range(N):
        total += C[i]*(B[i]-A[i])
    print(total)
