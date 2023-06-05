def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #print(n,a,b,c,d,e)
    if n % a == 0:
        ans = int(n/a) + 4
    else:
        ans = int(n/a) + 5
    print(ans)
