def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    if n == 0:
        print(x)
    else:
        for i in range(100):
            if x-i not in p:
                print(x-i)
                break
            if x+i not in p:
                print(x+i)
                break
