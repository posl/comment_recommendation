def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    print(W)
    for i in range(N):
        for j in range(i+1,N):
            if W[i] == W[j]:
                print("No")
                return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
