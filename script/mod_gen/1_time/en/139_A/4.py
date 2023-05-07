def main():
    s = input()
    t = input()
    print(sum(s[i] == t[i] for i in range(3)))

if __name__ == '__main__':
    main()