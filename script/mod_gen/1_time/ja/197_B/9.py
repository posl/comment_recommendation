def main():
    H,W,X,Y = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H,W,X,Y)
    #print(S[X-1][Y-1])
    if S[X-1][Y-1] == '#':
        print('0')
        return
    #print(S[X-1][Y-1])
    count = 1
    #print('count=',count)
    for i in range(1,100):
        if Y-1-i >= 0 and S[X-1][Y-1-i] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if Y-1+i < W and S[X-1][Y-1+i] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if X-1-i >= 0 and S[X-1-i][Y-1] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if X-1+i < H and S[X-1+i][Y-1] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    print(count)
    return

if __name__ == '__main__':
    main()