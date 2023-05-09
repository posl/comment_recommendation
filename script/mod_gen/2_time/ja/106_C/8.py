def main():
    S = input()
    K = int(input())
    s = S
    i = 0
    while i < K:
        if len(s) > K:
            print(s[K-1])
            break
        s = s.replace('1', '11')
        s = s.replace('2', '22')
        s = s.replace('3', '33')
        s = s.replace('4', '44')
        s = s.replace('5', '55')
        s = s.replace('6', '66')
        s = s.replace('7', '77')
        s = s.replace('8', '88')
        s = s.replace('9', '99')
        i += 1
    else:
        print(s[K-1])

if __name__ == '__main__':
    main()