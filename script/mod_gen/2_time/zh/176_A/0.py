def problems176_a():
    n,x,t = map(int, input().split())
    print((n+x-1)//x * t)

if __name__ == '__main__':
    problems176_a()