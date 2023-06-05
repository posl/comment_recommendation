def problem175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-k*d)
    else:
        x = x%d
        k = k-x//d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

if __name__ == '__main__':
    problem175_c()