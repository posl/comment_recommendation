def main():
    l,q = map(int,input().split())
    mark = [0] * (l+1)
    mark[1] = 1
    mark[l] = 1
    for i in range(q):
        c,x = map(int,input().split())
        mark[x] = 1
        if c == 1:
            for j in range(x+1,l+1):
                if mark[j] == 1:
                    print(j-x)
                    break
            for j in range(x-1,0,-1):
                if mark[j] == 1:
                    print(x-j)
                    break
        else:
            for j in range(x+1,l+1):
                if mark[j] == 1:
                    print(j-x)
                    break
            for j in range(x-1,0,-1):
                if mark[j] == 1:
                    print(x-j)
                    break
