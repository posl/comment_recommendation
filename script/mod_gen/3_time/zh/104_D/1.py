def main():
    s = input()
    #print(s)
    q = s.count('?')
    #print(q)
    #print(3**q)
    abc = 0
    for i in range(0, q+1):
        abc += 3**i * s.count('B?C') * 2**s.count('A?C') * 2**s.count('A?B') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc += 3**i * s.count('A?B') * 2**s.count('B?C') * 2**s.count('A?C') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc += 3**i * s.count('A?C') * 2**s.count('B?C') * 2**s.count('A?B') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc %= 10**9 + 7
    print(abc)

if __name__ == '__main__':
    main()