def main():
    n = int(input())
    a = 0
    b = 2*n+1
    while True:
        print((a+b)//2)
        a = int(input())
        if a == 0:
            break
        if a < (a+b)//2:
            b = (a+b)//2
        else:
            a = (a+b)//2
