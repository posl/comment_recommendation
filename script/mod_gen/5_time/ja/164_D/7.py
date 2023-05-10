def main():
    s = input()
    s_len = len(s)
    ans = 0
    for i in range(s_len):
        for j in range(i+3,s_len+1):
            num = int(s[i:j])
            if num % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()