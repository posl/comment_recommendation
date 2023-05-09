def main():
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            cnt += 1
        elif s[i] == 'w' and s[i+1] == 'w':
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()