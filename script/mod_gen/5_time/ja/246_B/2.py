def main():
    a,b = map(int, input().split())
    tmp = b/a
    #print(tmp)
    if a > b:
        tmp2 = (1-tmp**2)**0.5
        print(tmp2)
        print(1-tmp**2)
        print(tmp2)
        print(tmp)
    else:
        tmp2 = (1-tmp**2)**0.5
        print(tmp2)
        print(1-tmp**2)
        print(tmp2)
        print(tmp)

if __name__ == '__main__':
    main()