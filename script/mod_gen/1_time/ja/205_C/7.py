def pow(a,b):
    if b == 1:
        return a
    else:
        return a*pow(a,b-1)
A,B,C = map(int,input().split())

if __name__ == '__main__':
    pow()