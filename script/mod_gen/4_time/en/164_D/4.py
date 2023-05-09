def main():
    s = input()
    s_len = len(s)
    s_int = int(s)
    count = 0
    for i in range(s_len):
        for j in range(i, s_len):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()