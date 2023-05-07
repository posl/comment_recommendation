def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    #r1, c1, r2, c2 = 1, 1, 5, 6
    #r1, c1, r2, c2 = 1, 1, 1, 200001
    #r1, c1, r2, c2 = 2, 3, 998244353, 998244853
    #r1, c1, r2, c2 = 1, 1, 1, 1
    #print(r1, c1, r2, c2)
    #print(abs(r1 - r2), abs(c1 - c2))
    #print(abs(r1 - r2) + abs(c1 - c2))
    #print(abs(r1 - r2) + abs(c1 - c2) - 1)
    #print(abs(r1 - r2) + abs(c1 - c2) - 2)
    #print(abs(r1 - r2) + abs(c1 - c2) - 3)
    #print(abs(r1 - r2) + abs(c1 - c2) - 4)
    #print((r1 + c1) - (r2 + c2))
    #print((r1 - c1) - (r2 - c2))
    #print(abs((r1 + c1) - (r2 + c2)))
    #print(abs((r1 - c1) - (r2 - c2)))
    if r1 == r2 and c1 == c2:
        print(0)
    elif (r1 + c1) == (r2 + c2) or (r1 - c1) == (r2 - c2) or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) -

if __name__ == '__main__':
    main()