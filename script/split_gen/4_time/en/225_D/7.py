def main():
    #use sys.stdin.readline() instead of input()
    #to avoid TLE
    import sys
    n,q = map(int,sys.stdin.readline().split())
    train = [0]*n
    for i in range(n):
        train[i] = i+1
    for i in range(q):
        c,x,y = map(int,sys.stdin.readline().split())
        if c == 1:
            train[x-1] = train[y-1]
        elif c == 2:
            train[y-1] = y+1
        else:
            print(x,end=' ')
            temp = train[x-1]
            for j in range(x,n):
                if train[j] == temp:
                    print(j+1,end=' ')
            print()
