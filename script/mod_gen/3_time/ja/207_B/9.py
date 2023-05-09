def main():
    A,B,C,D = map(int, input().split())
    if B>D*C:
        print(-1)
        return
    if A<=B:
        print(0)
        return
    print((A-B)//(B-D*C)+1)

if __name__ == '__main__':
    main()