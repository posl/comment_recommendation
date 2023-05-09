def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, x, a)
    s = set()
    s.add(x-1)
    i = x-1
    while True:
        i = a[i]-1
        if i in s:
            break
        else:
            s.add(i)
    print(len(s))
