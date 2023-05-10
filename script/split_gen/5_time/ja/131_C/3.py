def main():
    a,b,c,d = map(int, input().split())
    e = c*d
    f = b//c - (a-1)//c
    g = b//d - (a-1)//d
    h = b//e - (a-1)//e
    print(b-a+1-f-g+h)
