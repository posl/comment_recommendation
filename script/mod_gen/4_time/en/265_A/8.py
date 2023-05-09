def main():
    X,Y,N = map(int, input().split())
    if N%X==0:
        print((N//X)*Y)
    else:
        print(((N//X)+1)*Y)

if __name__ == '__main__':
    main()