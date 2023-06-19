def main():
    L,Q = map(int,input().split())
    mark = [0]*L
    mark[0] = 1
    mark[-1] = 1
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x-1] = 1
        else:
            a = 0
            for j in range(x-1):
                if mark[j] == 1:
                    a = j+1
            b = 0
            for j in range(x-1,L-1):
                if mark[j] == 1:
                    b = j+1
                    break
            print(b-a)
