def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print(2*(h-1)*(w-1) - (h-1) - (w-1) + 1)
main()
