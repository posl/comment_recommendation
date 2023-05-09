def main():
    a,b,c,k = map(int,input().split())
    if k <= a:
        print(k)
        return
    elif k <= a+b:
        print(a)
        return
    else:
        print(a-(k-a-b))
        return
