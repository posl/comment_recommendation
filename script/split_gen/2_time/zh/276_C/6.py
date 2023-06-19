def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append(P.index(i+1)+1)
    print(*Q)
