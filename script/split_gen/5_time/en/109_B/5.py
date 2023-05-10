def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1, N):
        if W[i] in W[:i] or W[i-1][-1] != W[i][0]:
            print('No')
            exit()
    print('Yes')
