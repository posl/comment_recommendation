def main():
    N = input()
    S = sum(map(int, N))
    if S % 3 == 0:
        print(0)
    elif len(N) == 1:
        print(-1)
    elif S % 3 == 1:
        if N.count('1') >= 1 or N.count('4') >= 1 or N.count('7') >= 1:
            print(1)
        elif N.count('2') >= 2 or N.count('5') >= 2 or N.count('8') >= 2:
            print(2)
        elif N.count('3') >= 1 or N.count('6') >= 1 or N.count('9') >= 1:
            print(1)
        elif N.count('2') == 1 and N.count('5') == 1 and N.count('8') == 1:
            print(3)
        else:
            print(-1)
    else:
        if N.count('2') >= 1 or N.count('5') >= 1 or N.count('8') >= 1:
            print(1)
        elif N.count('1') >= 2 or N.count('4') >= 2 or N.count('7') >= 2:
            print(2)
        elif N.count('3') >= 1 or N.count('6') >= 1 or N.count('9') >= 1:
            print(1)
        elif N.count('1') == 1 and N.count('4') == 1 and N.count('7') == 1:
            print(3)
        else:
            print(-1)

if __name__ == '__main__':
    main()