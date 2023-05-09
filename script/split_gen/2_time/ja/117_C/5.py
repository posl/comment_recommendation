def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    #X = [-100000, -10, -3, 0, 2, 9, 17]
    #X = [-100000, -10, -3, 0, 2, 9, 17, 100000]
    diff = [X[i+1] - X[i] for i in range(M-1)]
    #print(diff)
    #diff = [90, 7, 3, 2, 7, 8]
    diff.sort()
    #print(diff)
    #diff = [2, 3, 7, 7, 8, 90]
    print(sum(diff[:M-N]))
