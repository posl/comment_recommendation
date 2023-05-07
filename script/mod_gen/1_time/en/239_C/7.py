def main():
    #input
    x1, y1, x2, y2 = map(int, input().split())
    #compute
    #output
    print(['No', 'Yes'][((x1-x2)**2+(y1-y2)**2)**.5%1==0])

if __name__ == '__main__':
    main()