def main():
    a,b,c,d = map(int,input().split())
    if a >= 0 and c >= 0:
        print(a*d)
    elif a >= 0 and d <= 0:
        print(a*c)
    elif b <= 0 and c >= 0:
        print(b*d)
    elif b <= 0 and d <= 0:
        print(b*c)
    else:
        print(max(a*c,a*d,b*c,b*d))
