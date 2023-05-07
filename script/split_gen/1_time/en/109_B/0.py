def main():
    N = int(input())
    W = [input() for i in range(N)]
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
        if W.count(W[i]) > 1:
            print("No")
            return
    print("Yes")
    return
