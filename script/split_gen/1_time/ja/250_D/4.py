def main():
    N = int(input())
    if N < 2:
        print(0)
        return
    if N < 5:
        print(1)
        return
    if N < 250:
        print(2)
        return
    if N < 625:
        print(3)
        return
    if N < 9375:
        print(4)
        return
    if N < 1953125:
        print(5)
        return
    if N < 244140625:
        print(6)
        return
    if N < 30517578125:
        print(7)
        return
    if N < 488281250000:
        print(8)
        return
    if N < 244140625000000:
        print(9)
        return
    if N < 152587890625000000:
        print(10)
        return
    print(11)
    
main()
