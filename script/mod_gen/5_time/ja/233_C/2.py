def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    #print(n, x)
    #print(l)
    #print(2**n)
    #for i in range(2**n):
    #    print(i)
    #print(bin(2**n))
    #print(bin(2**n)[2:])
    #print(len(bin(2**n)[2:]))
    #print(bin(2**n)[2:].zfill(n))
    #print(len(bin(2**n)[2:].zfill(n)))
    #print(bin(2**n)[2:].zfill(n)[::-1])
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1'))
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1)
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0)
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1)
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 2)
    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1 and bin(2**n)[2:].

if __name__ == '__main__':
    main()