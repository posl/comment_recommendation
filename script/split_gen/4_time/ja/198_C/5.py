def main():
    R,X,Y = map(int,input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5//R + 1))
