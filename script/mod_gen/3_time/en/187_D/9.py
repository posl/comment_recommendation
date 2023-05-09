def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #ABの中のBの値を小さい順にソートする
    AB.sort(key=lambda x:x[1], reverse=True)
    #print(AB)
    #Aの合計値
    Asum = 0
    #Bの合計値
    Bsum = 0
    #Bの合計値とAの合計値を比較して、Aの合計値が大きくなるまで
    #Bの合計値をAの合計値に足していく
    for i in range(N):
        Bsum += AB[i][1]
        Asum += AB[i][0]
        if Asum > Bsum:
            break
    print(i+1)

if __name__ == '__main__':
    main()