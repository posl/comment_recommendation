def main():
    s = input()
    print(s.count('o') * 100 + s.count('?') * 100 - s.count('o') * 10)

if __name__ == '__main__':
    main()