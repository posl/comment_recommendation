def main():
    #input
    a,b,c,d,e = map(int,input().split())
    #output
    if (a == b == c and d == e) or (a == b and c == d == e):
        print('Yes')
    else:
        print('No')
