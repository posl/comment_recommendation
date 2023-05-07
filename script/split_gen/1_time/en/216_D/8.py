def main():
    #入力
    N, M = map(int, input().split())
    #print(N, M)
    k = [0] * M
    a = [0] * M
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
        #print(k[i], a[i])
    #処理
    #print(a)
    #print(a[0][1])
    #print(a[1][1])
    #print(a[0][0])
    #print(a[1][0])
    #print(a[0][0] == a[1][0])
    #print(a[0][1] == a[1][1])
    #print(a[0][0] == a[0][1])
    #print(a[1][0] == a[1][1])
    #print(a[0][0] == a[1][1])
    #print(a[0][1] == a[1][0])
    #print(a[0][0] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] == a[0][0])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] == a[0][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] == a[1][0])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] == a[1][1])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] == a[0][1] == a[1][0])
    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1] ==
