def main():
    N,M = map(int, input().split())
    k = [0 for i in range(M)]
    a = [[0 for j in range(2*N)] for i in range(M)]
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    if M == 1:
        print("Yes")
        return
    #aの中身を見ていく
    color = [0 for i in range(N+1)]
    for i in range(M):
        for j in range(k[i]):
            color[a[i][j]] += 1
    #print(color)
    #ボールの個数が奇数ならNo
    for i in range(1,N+1):
        if color[i] % 2 == 1:
            print("No")
            return
    #ボールの個数が偶数ならYes
    print("Yes")
