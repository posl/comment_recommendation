def main():
    n,k = map(int,input().split())
    if k == n+1:
        print(1)
        return
    if k == 2:
        print(n*(n+1)//2)
        return
    if k == 3:
        print(n*(n+1)*(n+2)//6)
        return
    if k == 4:
        print(n*(n+1)*(n+2)*(n+3)//24)
        return
    if k == 5:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)//120)
        return
    if k == 6:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)//720)
        return
    if k == 7:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)//5040)
        return
    if k == 8:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)//40320)
        return
    if k == 9:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)//362880)
        return
    if k == 10:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)//3628800)
        return
    if k == 11:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)*(n+10)//39916800)
        return
    if k == 12:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)*(n+10)*(n+11)//479001600)
        return
    if k == 13:
        print(n*(n+1)*(n+2)*(n+3)*(

if __name__ == '__main__':
    main()