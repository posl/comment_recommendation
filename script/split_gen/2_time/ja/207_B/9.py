def main():
    A,B,C,D = map(int,input().split())
    i = 0
    while A>D*C:
        A += B
        A -= C
        i += 1
    if A<0:
        i = -1
    print(i)
