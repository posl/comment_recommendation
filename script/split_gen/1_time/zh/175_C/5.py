def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
    else:
        k -= x//d
        x %= d
        if k%2 == 0:
            print(x)
        else:
            print(abs(x-d))
