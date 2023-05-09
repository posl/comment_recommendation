def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        boxes = X[:]
        for j in range(L-1, R):
            boxes[j] = 0
        boxes = [box for box in boxes if box > 0]
        boxes.sort()
        Ws = W[:]
        Vs = V[:]
        Ws.sort()
        Vs.sort()
        Ws.reverse()
        Vs.reverse()
        ans = 0
        for box in boxes:
            for j in range(N):
                if Ws[j] <= box:
                    ans += Vs[j]
                    Ws[j] = 10**6+1
                    Vs[j] = 0
                    break
        print(ans)
