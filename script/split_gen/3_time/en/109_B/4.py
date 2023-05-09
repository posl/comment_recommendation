def main():
    N = int(input())
    W = [input() for i in range(N)]
    if len(W) != len(set(W)):
        print('No')
        return
    for i in range(1, N):
        if W[i-1][-1] != W[i][0]:
            print('No')
            return
    print('Yes')
