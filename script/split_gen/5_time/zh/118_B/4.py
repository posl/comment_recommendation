def main():
    N,M = map(int,input().split())
    K = []
    A = []
    for i in range(N):
        K.append(list(map(int,input().split()))[1:])
        A += K[i]
    A.sort()
    count = 0
    for i in range(M):
        if A.count(i+1) == N:
            count += 1
    print(count)
