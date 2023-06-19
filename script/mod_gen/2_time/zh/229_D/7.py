def main():
    s = input()
    k = int(input())
    s = s.replace('X', 'XX')
    s = s.replace('.', 'X')
    s = s.replace('X', '.')
    s = s.replace('..', '.')
    s = s.replace('X', 'XX')
    print(min(len(s), len(s) + k))

if __name__ == '__main__':
    main()