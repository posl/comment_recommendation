def main():
    a,b,c,d = map(int,input().split())
    if a > c*d:
        print(-1)
        return
    else:
        if a <= b:
            print(1)
            return
        else:
            print((a-b-1)//(b-c)+2)
            return
