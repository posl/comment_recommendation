def main():
    a,b = map(int,input().split())
    if a>b:
        tmp = a
        a = b
        b = tmp
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSSIBLE")
