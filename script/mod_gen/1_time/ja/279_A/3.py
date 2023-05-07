def main():
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'v':
            if s[i+1] == 'v':
                cnt += 1
            else:
                cnt += 2
    print(cnt)

if __name__ == '__main__':
    main()