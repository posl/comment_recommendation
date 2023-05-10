def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    if x not in p:
        print(x)
        return
    for i in range(1,100):
        if x - i not in p:
            print(x-i)
            return
        elif x + i not in p:
            print(x+i)
            return
