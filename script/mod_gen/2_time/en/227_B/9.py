def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    #print(n)
    #print(s)
    #print(s.count(1))
    #print(s.count(4))
    #print(s.count(3))
    #print(s.count(2))
    #print(s.count(1))
    if s.count(4) == 1 and s.count(3) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(0)
    elif s.count(4) == 1 and s.count(3) == 1 and s.count(2) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(3) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(3) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(3) == 1:
        print(2)
    elif s.count(4) == 1 and s.count(2) == 1:
        print(2)
    elif s.count(4) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(3) == 1 and s.count(2) == 1:
        print(2)
    elif s.count(3) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(2) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(4) == 1:
        print(3)
    elif s.count(3) == 1:
        print(3)
    elif s.count(2) == 1:
        print(3)
    elif s.count(1) == 1:
        print(3)
    else:
        print(4)

if __name__ == '__main__':
    main()