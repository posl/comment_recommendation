def main():
    s = input()
    cnt = 0
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()