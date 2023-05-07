def main():
    #入力
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    #処理
    #最大値を求める
    A.sort()
    #print(A)
    max = A[-1]
    #print(max)
    #最大値の個数を求める
    cnt = 0
    for i in range(N):
        if A[i] == max:
            cnt += 1
    #print(cnt)
    #出力
    if cnt == 1:
        for i in range(N):
            if A[i] == max:
                print(max)
            else:
                print(max)
    else:
        for i in range(N):
            print(max)
main()

if __name__ == '__main__':
    main()