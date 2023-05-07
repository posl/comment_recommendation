def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    b = sorted(a)
    #print(b)
    c = b[1]
    #print(c)
    d = a.index(c) + 1
    print(d)
