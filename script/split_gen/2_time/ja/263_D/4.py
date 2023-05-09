def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    #累積和
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i]+A[i])
    #print(sumA)
    #最小値
    minA = sumA[N]
    #print(minA)
    #x=0,y=0
    if minA > L:
        minA = L
    if minA > R:
        minA = R
    #print(minA)
    #x=1,y=1
    for i in range(1, N+1):
        if minA > L + sumA[i]:
            minA = L + sumA[i]
        if minA > R + sumA[N]-sumA[N-i]:
            minA = R + sumA[N]-sumA[N-i]
    #print(minA)
    #x=0,y=1
    for i in range(1, N+1):
        if minA > R + sumA[N]-sumA[N-i]:
            minA = R + sumA[N]-sumA[N-i]
    #print(minA)
    #x=1,y=0
    for i in range(1, N+1):
        if minA > L + sumA[i]:
            minA = L + sumA[i]
    #print(minA)
    #x=0,y=2
    for i in range(1, N):
        if minA > 2*R + sumA[N]-sumA[N-i]:
            minA = 2*R + sumA[N]-sumA[N-i]
    #print(minA)
    #x=2,y=0
    for i in range(1, N):
        if minA > 2*L + sumA[i]:
            minA = 2*L + sumA[i]
    #print(minA)
    #x=1,y=2
    for i in range(1, N):
        for j in range(1, N-i+1):
            if minA > L + 2*R + sumA[N]-sumA[N-i]-sumA[N-i-j]:
                minA = L + 2
