def main():
    s = input()
    if len(s) == len(set(s)) and s.islower() == False:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()