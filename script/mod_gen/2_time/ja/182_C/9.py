def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    n = len(N)
    ans = -1
    #print(N)
    #print(n)
    #print(sum(N))
    #print(sum(N) % 3)
    if sum(N) % 3 == 0:
        ans = 0
    else:
        if n == 1:
            ans = -1
        else:
            if sum(N) % 3 == 1:
                if N.count(1) >= 1:
                    ans = 1
                elif N.count(4) >= 1:
                    ans = 1
                elif N.count(7) >= 1:
                    ans = 1
                elif N.count(10) >= 1:
                    ans = 1
                elif N.count(13) >= 1:
                    ans = 1
                elif N.count(16) >= 1:
                    ans = 1
                elif N.count(19) >= 1:
                    ans = 1
                elif N.count(22) >= 1:
                    ans = 1
                elif N.count(25) >= 1:
                    ans = 1
                elif N.count(28) >= 1:
                    ans = 1
                elif N.count(31) >= 1:
                    ans = 1
                elif N.count(34) >= 1:
                    ans = 1
                elif N.count(37) >= 1:
                    ans = 1
                elif N.count(40) >= 1:
                    ans = 1
                elif N.count(43) >= 1:
                    ans = 1
                elif N.count(46) >= 1:
                    ans = 1
                elif N.count(49) >= 1:
                    ans = 1
                elif N.count(52) >= 1:
                    ans = 1
                elif N.count(55) >= 1:
                    ans = 1
                elif N.count(58) >= 1:
                    ans = 1
                elif N.count(61) >= 1:
                    ans = 1
                elif N.count(64) >= 1:
                    ans = 1
                elif N.count(67) >= 1:
                    ans =

if __name__ == '__main__':
    main()