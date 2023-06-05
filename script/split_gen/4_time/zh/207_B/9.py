def main():
    a,b,c,d = map(int,input().split())
    if a < b:
        print(-1)
        return
    if d == 1:
        if a > b:
            print(1)
            return
        else:
            print(-1)
            return
    if (a-b)%(b-c) == 0:
        print((a-b)//(b-c)+1)
    else:
        print((a-b)//(b-c)+2)
