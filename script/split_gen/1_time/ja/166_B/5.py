def main():
    # input
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    # compute
    count = 0
    for i in range(N):
        flag = True
        for j in range(K):
            if i+1 in A[j]:
                flag = False
        if flag:
            count += 1
    # output
    print(count)
