def main():
    s = input()
    # s = '1817181712114'
    # s = '14282668646'
    # s = '2119'
    count = 0
    for i in range(0, len(s)-3):
        if int(s[i:i+4]) % 2019 == 0:
            count += 1
            print(s[i:i+4])
    print(count)

if __name__ == '__main__':
    main()