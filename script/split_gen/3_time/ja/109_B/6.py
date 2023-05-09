def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    #print(W)
    for i in range(N-1):
        if W[i] in W[i+1:]:
            print("No")
            return
        elif W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
    return
