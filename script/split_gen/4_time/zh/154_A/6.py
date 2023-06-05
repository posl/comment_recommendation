def main():
    s,t = map(str,input().split())
    a,b = map(int,input().split())
    u = str(input())
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,b)
