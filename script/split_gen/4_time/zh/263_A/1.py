def main():
    a,b,c,d,e = map(int,input().split())
    if a == b == c or a == b == d or a == b == e or a == c == d or a == c == e or a == d == e or b == c == d or b == c == e or b == d == e or c == d == e:
        print('Yes')
    else:
        print('No')
