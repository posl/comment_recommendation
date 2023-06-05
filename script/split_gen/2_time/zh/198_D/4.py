def main():
    r,x,y = map(int,input().split())
    if (x**2 + y**2) % (r**2) == 0:
        print((x**2 + y**2) // (r**2))
    else:
        print((x**2 + y**2) // (r**2) + 1)
