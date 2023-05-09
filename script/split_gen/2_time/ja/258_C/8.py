def main():
    n,q = map(int,input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            x = x - 1
            s = s[-x:] + s[:-x]
            #print(s)
        elif t == 2:
            x = x - 1
            print(s[x])
        else:
            print("error")
