def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    #print(N)
    #print(W)
    if len(set(W)) != N:
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
