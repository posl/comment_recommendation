def main():
    l,q = map(int,input().split())
    mark = [0 for i in range(l+1)]
    mark[0] = 1
    mark[l] = 1
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = 1
        else:
            for j in range(x,0,-1):
                if mark[j] == 1:
                    left = j
                    break
            for j in range(x,l+1):
                if mark[j] == 1:
                    right = j
                    break
            print(right-left)
main()
