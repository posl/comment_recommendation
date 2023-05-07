def main():
    s = input()
    s = s.replace(s, 'x' * len(s))
    print(s)

if __name__ == '__main__':
    main()