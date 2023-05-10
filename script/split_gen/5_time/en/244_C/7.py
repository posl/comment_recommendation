def main():
    n = int(input())
    a = 0
    b = 2*n+2
    while True:
        c = (a+b)//2
        print(c)
        s = int(input())
        if s == 0:
            break
        elif (s == 1 and c == a+1) or (s == 2 and c == b-1):
            a = c
        else:
            b = c
