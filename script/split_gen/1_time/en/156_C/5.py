def main():
    N = int(input())
    X = list(map(int,input().split()))
    X.sort()
    tmp = 0
    for i in range(N):
        tmp += abs(i+1-X[i])
    print(tmp)
