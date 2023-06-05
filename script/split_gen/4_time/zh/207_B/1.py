def main():
    a,b,c,d = map(int, input().split())
    if a <= b*d:
        print(-1)
    else:
        print((a*d+b-1)//b-c)
