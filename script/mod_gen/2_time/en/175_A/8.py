def main():
    s = input()
    print(max(len(x) for x in s.split('S')))

if __name__ == '__main__':
    main()