def main():
    s = input()
    s = s.replace('A', 'a')
    s = s.replace('C', 'c')
    s = s.replace('G', 'g')
    s = s.replace('T', 't')
    s = s.split('a')
    s = s.split('c')
    s = s.split('g')
    s = s.split('t')
    print(s)
main()

if __name__ == '__main__':
    main()