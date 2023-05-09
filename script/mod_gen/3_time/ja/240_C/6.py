def main():
    #入力
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(N,X,a,b)
    #処理
    #print(sum(a))
    if sum(a) > X:
        print("No")
        exit()
    if sum(b) < X:
        print("No")
        exit()
    else:
        print("Yes")
        exit()

if __name__ == '__main__':
    main()