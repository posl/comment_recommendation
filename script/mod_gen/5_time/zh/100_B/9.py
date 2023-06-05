def problems100_b():
    d,n = map(int, input().split())
    if d == 0:
        print(n if n < 100 else 101**n)
    elif d == 1:
        print(n*100 if n < 100 else 10100**n)
    else:
        print(n*10000 if n < 100 else 1010000**n)

if __name__ == '__main__':
    problems100_b()