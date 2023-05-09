def main():
    #input
    AB, BC, CA = map(int, input().split())
    #processing
    area = (AB*BC)//2
    #output
    print(area)

if __name__ == '__main__':
    main()