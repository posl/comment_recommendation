def main():
    a,b,c,d = map(int,input().split())
    if a > c*d:
        print(-1)
    else:
        print((c*d-a-1)//(b-c)+1)
