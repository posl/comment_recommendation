def main():
    s = input()
    r = s.replace('S', '0')
    r = r.replace('R', '1')
    r = r.replace('0', 'R')
    r = r.replace('1', 'S')
    print(r.count('R'))

if __name__ == '__main__':
    main()