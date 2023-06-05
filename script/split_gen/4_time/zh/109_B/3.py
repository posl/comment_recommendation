def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1, N):
        if W[i] in W[:i]:
            print("No")
            return
        if W[i][0] != W[i - 1][-1]:
            print("No")
            return
    print("Yes")
