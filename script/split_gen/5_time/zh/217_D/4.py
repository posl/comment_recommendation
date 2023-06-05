def main():
    L,Q = map(int,input().split())
    mark = [0]*(L+1)
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = 1
        else:
            if mark[x] == 1:
                mark[x] = 0
                left = 0
                right = 0
                for j in range(x+1,L+1):
                    if mark[j] == 0:
                        right = j
                        break
                for j in range(x-1,-1,-1):
                    if mark[j] == 0:
                        left = j
                        break
                print(right-left)
            else:
                print(0)
