def main():
    X,Y,N = map(int,input().split())
    # 3個買う方がお得かどうか
    if X*3 < Y:
        print(N*X)
    else:
        # 3個買う方がお得なので、3個単位でまとめて買う
        # 3個単位で買うためには、Nを3で割ったあまりが0か1か2かで場合分け
        if N%3 == 0:
            print((N//3)*Y)
        elif N%3 == 1:
            print((N//3)*Y+X)
        else:
            print((N//3)*Y+X*2)
