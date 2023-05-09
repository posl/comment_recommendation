def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = list(map(int,N))
    sum = 0
    for i in range(len(N)):
        sum += N[i]
    if sum % 3 == 0:
        print(0)
    elif sum % 3 == 1:
        if 1 in N:
            N.remove(1)
            print(len(N))
        elif 4 in N:
            N.remove(4)
            print(len(N))
        elif 7 in N:
            N.remove(7)
            print(len(N))
        elif 10 in N:
            N.remove(10)
            print(len(N))
        elif 13 in N:
            N.remove(13)
            print(len(N))
        elif 16 in N:
            N.remove(16)
            print(len(N))
        elif 19 in N:
            N.remove(19)
            print(len(N))
        elif 22 in N:
            N.remove(22)
            print(len(N))
        elif 25 in N:
            N.remove(25)
            print(len(N))
        elif 28 in N:
            N.remove(28)
            print(len(N))
        elif 31 in N:
            N.remove(31)
            print(len(N))
        elif 34 in N:
            N.remove(34)
            print(len(N))
        elif 37 in N:
            N.remove(37)
            print(len(N))
        elif 40 in N:
            N.remove(40)
            print(len(N))
        elif 43 in N:
            N.remove(43)
            print(len(N))
        elif 46 in N:
            N.remove(46)
            print(len(N))
        elif 49 in N:
            N.remove(49)
            print(len(N))
        elif 52 in N:
            N.remove(52)
            print(len(N))
        elif 55 in N:
            N.remove(55)
            print(len(N))
        elif 58 in N:
            N.remove(58)
            print(len(N))
        elif 61 in N:
            N.remove(61)
            print(len(N))
        elif 64 in N:
            N.remove(64)
            print(len(N))
        elif 67 in N:
            N.remove(67)
            print(len(N))
        elif 70 in N:
            N.remove(70)

if __name__ == '__main__':
    main()