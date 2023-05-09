def main():
    #input
    v,a,b,c = map(int,input().split())
    #process
    if v - a < 0:
        print("F")
    elif v - a - b < 0:
        print("M")
    elif v - a - b - c < 0:
        print("T")
    else:
        print("M")

if __name__ == '__main__':
    main()