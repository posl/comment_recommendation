def main():
    #read input
    AB, BC, CA = map(int, input().split())
    #calculation
    S = (AB * BC) // 2
    #output
    print(S)

if __name__ == '__main__':
    main()