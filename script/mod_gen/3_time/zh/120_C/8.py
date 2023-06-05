def main():
    s = input()
    print(s.count('0')*2 if s.count('0') < s.count('1') else s.count('1')*2)

if __name__ == '__main__':
    main()