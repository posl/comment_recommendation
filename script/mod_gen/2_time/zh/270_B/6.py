def main():
    x,y,z = map(int,input().split())
    if x < y < z:
        print(z-y)
    else:
        print(-1)
main()
