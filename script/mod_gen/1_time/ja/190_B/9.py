def check():
    N,S,D = map(int, input().split())
    ret = "No"
    for i in range(N):
        X,Y = map(int, input().split())
        if X < S and Y > D:
            ret = "Yes"
    print(ret)

if __name__ == '__main__':
    check()