def main():
    n,a,b = map(int,input().split())
    for i in range(a*n):
        if i%2 == 0:
            print("."*b + "#"*b)
        else:
            print("#"*b + "."*b)

if __name__ == '__main__':
    main()