def main():
    H, M = map(int, input().split())
    if H >= 0 and H <= 23 and M >= 0 and M <= 59:
        if M == 59:
            if H == 23:
                H = 0
                M = 0
            else:
                H += 1
                M = 0
        else:
            M += 1
        if H == 0:
            H = '00'
        if M == 0:
            M = '00'
        if H == 1 or H == 2 or H == 5 or H == 6 or H == 8 or H == 11 or H == 12 or H == 15 or H == 16 or H == 18 or H == 21 or H == 22:
            print(str(H) + ' ' + str(M))
        elif H == 3 or H == 4 or H == 7 or H == 9 or H == 13 or H == 14 or H == 17 or H == 19 or H == 23:
            if M == 10 or M == 20 or M == 30 or M == 40 or M == 50:
                print(str(H) + ' ' + str(M))
            elif M == 1 or M == 2 or M == 5 or M == 6 or M == 8 or M == 11 or M == 12 or M == 15 or M == 16 or M == 18 or M == 21 or M == 22 or M == 25 or M == 26 or M == 28 or M == 31 or M == 32 or M == 35 or M == 36 or M == 38 or M == 41 or M == 42 or M == 45 or M == 46 or M == 48 or M == 51 or M == 52 or M == 55 or M == 56 or M == 58:
                print(str(H) + ' ' + str(M))
            elif M == 3 or M == 4 or M == 7 or M == 9 or M == 13 or M == 14 or M == 17 or M == 19 or M == 23 or M == 24 or M == 27 or M == 29 or M ==

if __name__ == '__main__':
    main()