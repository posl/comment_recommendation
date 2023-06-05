def main():
    line = input()
    l,r = line.split()
    l = int(l)
    r = int(r)
    atcoder = 'atcoder'
    print(atcoder[l-1:r])

if __name__ == '__main__':
    main()