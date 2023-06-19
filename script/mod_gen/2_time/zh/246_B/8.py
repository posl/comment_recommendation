def problems246_b():
    A,B = map(int,input().split())
    x = A/(A**2+B**2)**0.5
    y = B/(A**2+B**2)**0.5
    print(x,y)

if __name__ == '__main__':
    problems246_b()