def main():
    s = input()
    r = s.count('0')
    b = s.count('1')
    print(min(r,b)*2)

if __name__ == '__main__':
    main()