def main():
    a,b,c,d,e = map(int,input().split())
    if a==b==c==d==e:
        print(1)
    elif a==b==c==d or a==b==c==e or a==b==d==e or a==c==d==e or b==c==d==e:
        print(2)
    elif a==b==c or a==b==d or a==b==e or a==c==d or a==c==e or a==d==e or b==c==d or b==c==e or b==d==e or c==d==e:
        print(3)
    else:
        print(5)
