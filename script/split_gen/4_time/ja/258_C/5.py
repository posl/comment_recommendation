def main():
    n, q = map(int, input().split())
    s = input()
    #print(n, q)
    #print(s)
    for i in range(q):
        t, x = map(int, input().split())
        #print(t, x)
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])
