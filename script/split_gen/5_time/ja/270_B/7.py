def main():
    x,y,z = map(int,input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(abs(x-y)+z)
    else:
        print(x-y+z)
