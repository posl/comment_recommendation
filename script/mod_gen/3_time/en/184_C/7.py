def main():
    #input
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    #output
    #r1,c1からr2,c2に移動するのに最短何手か
    #1手で移動できるのは、以下の8通り
    # (r1+c1) = (r2+c2)
    # (r1-c1) = (r2-c2)
    # |r1-r2|+|c1-c2| <= 3
    # ただし、このうち、3通りは2手で移動できる
    # つまり、以下の5通りのうち、最小のものが答え
    # (r1+c1) = (r2+c2)
    # (r1-c1) = (r2-c2)
    # |r1-r2|+|c1-c2| = 1
    # |r1-r2|+|c1-c2| = 2
    # |r1-r2|+|c1-c2| = 3
    # ただし、(r1,c1) = (r2,c2)のときは、0手で移動できる
    if (r1,c1) == (r2,c2):
        print(0)
    elif (r1+c1) == (r2+c2) or (r1-c1) == (r2-c2) or abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
    else:
        # 4通りのうち、|r1-r2|+|c1-c2| = 4のときは、2手で移動できる
        if abs(r1-r2)+abs(c1-c2) == 4:
            print(2)
        # 4通りのうち、|r1-r2|+|c1-c2| > 4のときは、3手で移動できる
        else:
            print(3)

if __name__ == '__main__':
    main()