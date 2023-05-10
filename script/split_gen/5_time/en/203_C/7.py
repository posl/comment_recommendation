def main():
    N, K = map(int, input().split())
    #print(N, K)
    A = []
    B = []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    money = K
    village = 0
    while money > 0:
        #print(money, village)
        for n in range(N):
            if A[n] == village:
                money += B[n]
        village += 1
        money -= 1
    print(village - 1)
