def main():
    #print('Start...')
    p = list(map(int, input().split()))
    #print(p)
    #print(type(p))
    #print(p[0])
    #print(p[25])
    #print(chr(97))
    #print(chr(65))
    #print(ord('a'))
    #print(ord('z'))
    for i in range(26):
        #print(p[i])
        #print(chr(p[i]+96))
        print(chr(p[i]+96), end='')
    print()

if __name__ == '__main__':
    main()