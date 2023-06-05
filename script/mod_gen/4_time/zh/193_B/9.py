def getMinMoney(N, A, P, X):
    minMoney = -1
    for i in range(N):
        if X[i] > 0:
            money = P[i]
            if minMoney == -1:
                minMoney = money
            else:
                minMoney = min(minMoney, money)
    return minMoney
N = int(input())
A = []
P = []
X = []
for i in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)
minMoney = getMinMoney(N, A, P, X)
print(minMoney)

if __name__ == '__main__':
    getMinMoney()