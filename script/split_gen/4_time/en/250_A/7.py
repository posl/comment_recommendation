def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-1)+(w-1)+(h-1)*(w-1)-2*(r-1)-2*(c-1))
main()
