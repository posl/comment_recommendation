def main():
    N = int(input())
    P = []
    for i in range(N):
        P.append([int(j) for j in input().split()])
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == "L":
            L.append(P[i])
        else:
            R.append(P[i])
    L = sorted(L, key=lambda x: x[0])
    R = sorted(R, key=lambda x: x[0], reverse=True)
    for i in range(len(L)-1):
        if L[i][1] < L[i+1][1]:
            print("Yes")
            exit()
    for i in range(len(R)-1):
        if R[i][1] < R[i+1][1]:
            print("Yes")
            exit()
    if len(L) == 0 or len(R) == 0:
        print("No")
        exit()
    if L[-1][1] > R[0][1]:
        print("Yes")
    else:
        print("No")
