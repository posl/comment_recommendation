def main():
    L,Q = map(int,input().split())
    mark = [0] * L
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x-1] = 1
        else:
            if mark[x-1] == 1:
                mark[x-1] = 0
                print(L)
            else:
                for j in range(x-1,L):
                    if mark[j] == 1:
                        len = j - x + 1
                        print(len)
                        break
