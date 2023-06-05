def problem250_a():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

if __name__ == '__main__':
    problem250_a()