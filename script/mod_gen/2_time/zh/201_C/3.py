def main():
    s = input()
    n = 0
    for i in range(10):
        if s[i] == 'o':
            n += 1
    print(1000*n + 100*(s.count('?')-n))

if __name__ == '__main__':
    main()