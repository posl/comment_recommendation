def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    for i in range(X+1):
        for j in range(X-i+1):
            if i*2+j*4 == Y:
                print("Yes")
                return
    print("No")
