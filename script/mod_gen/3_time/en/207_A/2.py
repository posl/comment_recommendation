def main():
    a,b,c = [int(x) for x in input().split()]
    print(max(a+b,a+c,b+c))
main()
