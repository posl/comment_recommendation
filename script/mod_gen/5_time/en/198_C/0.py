def problems198_c():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 == R**2:
        print(1)
    elif X**2 + Y**2 <= R**2*2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5//R)+1)

if __name__ == '__main__':
    problems198_c()