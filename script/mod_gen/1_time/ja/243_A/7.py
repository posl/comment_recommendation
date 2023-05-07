def main():
    V,A,B,C = map(int,input().split())
    if V%A == 0:
        if V%B == 0:
            if V%C == 0:
                print("M")
            else:
                print("T")
        else:
            print("F")
    else:
        print("F")

if __name__ == '__main__':
    main()