def main():
    s = input()
    v_count = 0
    w_count = 0
    bottom_count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v_count += 1
            bottom_count += w_count
        else:
            w_count += 1
    print(bottom_count)

if __name__ == '__main__':
    main()