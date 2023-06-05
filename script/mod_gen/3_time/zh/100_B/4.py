def problems100_b():
    d,n = map(int,input().split())
    if n == 100:
        n = 101
    if d == 0:
        print(n)
    elif d == 1:
        print(n*100)
    else:
        print(n*10000)

if __name__ == '__main__':
    problems100_b()