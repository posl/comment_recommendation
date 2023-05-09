def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    #print(P)
    R = []
    for i in range(N):
        R.append(sum(P[i]))
    #print(R)
    R.sort(reverse=True)
    #print(R)
    for i in range(K):
        if R[i] < 300 * 4:
            print("Yes")
        else:
            print("No")
main()
