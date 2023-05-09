def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            count += 1
        elif s[i] == 'w' and s[i+1] == 'w':
            count += 1
    print(count)

if __name__ == '__main__':
    main()