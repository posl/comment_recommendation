def main():
    s = input()
    t = input()
    print('Yes' if len(set(s)) == len(set(t)) else 'No')

if __name__ == '__main__':
    main()